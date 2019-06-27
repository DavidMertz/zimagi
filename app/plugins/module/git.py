from django.conf import settings

from db_mutex import DBMutexError, DBMutexTimeoutError
from db_mutex.db_mutex import db_mutex

from .base import BaseProvider

import pygit2
import shutil
import pathlib
import os


class Provider(BaseProvider):

    def provider_config(self, type = None):
        self.requirement(str, 'remote', help = 'Git remote to clone and pull updates')

        self.option(str, 'reference', 'master', help = 'Git branch, tag, or commit reference', config_name = 'git_reference')


    def initialize_instance(self, instance, created):
        try:
            with db_mutex("git-initialize-{}".format(instance.name)):
                module_path = self.module_path(instance.name)
                git_path = os.path.join(module_path, '.git')

                if not os.path.isdir(git_path):
                    self._init_repository(instance, module_path)
                self._update_repository(instance, module_path)

        except DBMutexError:
            self.command.warning("Could not obtain {} Git lock".format(instance.name))
        except DBMutexTimeoutError:
            self.command.warning("Git lock timed out for {}".format(instance.name))

    def _init_repository(self, instance, module_path):
        if (os.path.exists(os.path.join(module_path, '.git'))):
            repository = pygit2.Repository(module_path)
            repository.remotes.set_url("origin", instance.remote)
            self._pull(repository, branch_name = instance.reference)
        else:
            repository = pygit2.clone_repository(instance.remote, module_path, checkout_branch = instance.reference)

        repository.update_submodules(init = True)
        self.command.success("Initialized repository from remote")

    def _update_repository(self, instance, module_path):
        repository = pygit2.Repository(module_path)
        repository.remotes.set_url("origin", instance.remote)

        self._pull(repository, branch_name = instance.reference)
        repository.update_submodules(init = True)
        self.command.success("Updated repository from remote")


    def finalize_instance(self, instance):
        try:
            with db_mutex("git-finalize-{}".format(instance.name)):
                module_path = self.module_path(instance.name)
                shutil.rmtree(pathlib.Path(module_path), ignore_errors = True)

        except DBMutexError:
            self.command.warning("Could not obtain {} Git lock".format(instance.name))
        except DBMutexTimeoutError:
            self.command.warning("Git lock timed out for {}".format(instance.name))


    def _pull(self, repository, remote_name = 'origin', branch_name = 'master'):
        repository.checkout(repository.lookup_branch(branch_name))

        remote = repository.remotes[remote_name]
        remote.fetch()

        remote_reference = repository.lookup_reference('refs/remotes/{}/{}'.format(remote_name, branch_name)).target
        merge_result, _ = repository.merge_analysis(remote_reference)

        if merge_result & pygit2.GIT_MERGE_ANALYSIS_UP_TO_DATE:
            return

        elif merge_result & pygit2.GIT_MERGE_ANALYSIS_FASTFORWARD:
            repository.checkout_tree(repository.get(remote_reference))
            head_reference = repository.lookup_reference('refs/heads/{}'.format(branch_name))
            head_reference.set_target(remote_reference)
            repository.head.set_target(remote_reference)

        elif merge_result & pygit2.GIT_MERGE_ANALYSIS_NORMAL:
            repository.merge(remote_reference)
            user = repository.default_signature
            tree = repository.index.write_tree()
            commit = repository.create_commit('HEAD',
                user,
                user,
                'Merge',
                tree,
                [repository.head.target, remote_reference]
            )
            repository.state_cleanup()

        else:
            self.command.error("Unable to pull remote changes from remote")
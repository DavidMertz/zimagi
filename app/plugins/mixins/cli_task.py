from systems.plugins.index import ProviderMixin
from plugins.parser.config import ConfigTemplate
from utility.data import ensure_list, env_value


class CLITaskMixin(ProviderMixin('cli_task')):

    def _env_vars(self, params):
        return self.command.options.interpolate(env_value(self._merge_options(
            self.field_env,
            params.pop('env', {})
        )))

    def _merge_options(self, options, overrides, lock = False):
        if not lock and overrides:
            return { **options, **overrides }
        return options

    def _interpolate(self, command, variables):
        final_command = []
        variables = self.command.options.interpolate(variables)

        for component in ensure_list(command):
            parser = ConfigTemplate(component)
            try:
                final_command.append(parser.substitute(**variables).strip())
            except KeyError as e:
                self.command.error("Configuration {} does not exist, escape literal with @@".format(e))

        return final_command

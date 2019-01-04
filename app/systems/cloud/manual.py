from .base import BaseCloudProvider


class Manual(BaseCloudProvider):

    def provider_config(self):
        self.requirement('region', help = 'Region name of server')
        self.requirement('name', help = 'Unique name of server in environment')
        self.requirement('ip', help = 'SSH capable IP of server')
        self.requirement('password', help = 'Password of server user')

        self.option('user', 'admin', help = 'Server SSH user')
        self.option('data_device', '/dev/sda4', help = 'Server data drive device')


    def create_server(self, index, server):
        if not self.check_ssh(server = server):
            self.command.error("Can not establish SSH connection to: {}".format(server))

from .base import BaseComputeProvider


class Manual(BaseComputeProvider):

    def provider_config(self):
        self.requirement('region', help = 'Region name of server', config_name = 'manual_region')
        self.requirement('zone', help = 'Zone name of server', config_name = 'manual_zone')
        self.requirement('name', help = 'Unique name of server in environment')
        self.requirement('ip', help = 'SSH capable IP of server')
        self.requirement('password', help = 'Password of server user')

        self.option('user', 'admin', help = 'Server SSH user', config_name = 'manual_user')
        self.option('data_device', '/dev/sda4', help = 'Server data drive device', config_name = 'manual_data_device')


    def create_server(self, index, server):
        if not self.check_ssh(server = server):
            self.command.error("Can not establish SSH connection to: {}".format(server))

from systems.command import types
from data.config.management.commands import _config as config


class Command(types.ConfigRouterCommand):

    def get_command_name(self):
        return 'config'

    def get_description(self, overview):
        if overview:
            return """manage environment configurations

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam 
pulvinar nisl ac magna ultricies dignissim. Praesent eu feugiat 
elit. Cras porta magna vel blandit euismod.
"""
        else:
            return """manage environment configurations
                      
Etiam mattis iaculis felis eu pharetra. Nulla facilisi. 
Duis placerat pulvinar urna et elementum. Mauris enim risus, 
mattis vel risus quis, imperdiet convallis felis. Donec iaculis 
tristique diam eget rutrum.

Etiam sit amet mollis lacus. Nulla pretium, neque id porta feugiat, 
erat sapien sollicitudin tellus, vel fermentum quam purus non sem. 
Mauris venenatis eleifend nulla, ac facilisis nulla efficitur sed. 
Etiam a ipsum odio. Curabitur magna mi, ornare sit amet nulla at, 
scelerisque tristique leo. Curabitur ut faucibus leo, non tincidunt 
velit. Aenean sit amet consequat mauris.
"""
    def get_subcommands(self):
        return (
            ('list', config.ListCommand),
            ('get', config.GetCommand),
            ('set', config.SetCommand),
            ('rm', config.RemoveCommand),
            ('clear', config.ClearCommand),
            ('group', config.GroupCommand)
        )
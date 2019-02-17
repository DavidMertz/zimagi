from systems.command import types, mixins


class UpdateCommand(
    types.NetworkFirewallActionCommand
):
    def get_description(self, overview):
        if overview:
            return """update an existing firewall in environment network

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam 
pulvinar nisl ac magna ultricies dignissim. Praesent eu feugiat 
elit. Cras porta magna vel blandit euismod.
"""
        else:
            return """update an existing firewall in environment network
                      
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
    def parse(self):
        self.parse_test()
        self.parse_force()
        self.parse_network_name('--network')
        self.parse_firewall_name()
        self.parse_firewall_fields(True, self.get_provider('network', 'help').field_help)

    def exec(self):
        self.set_firewall_scope()
        self.firewall.provider.update(self.firewall_fields)

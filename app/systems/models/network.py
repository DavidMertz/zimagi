from django.db import models as django

from data.network.models import Network
from .resource import ResourceModel, ResourceModelFacadeMixin


class NetworkModelFacadeMixin(ResourceModelFacadeMixin):

    def set_scope(self, network):
        super().set_scope(network_id = network.id)


class NetworkMixin(django.Model):
    
    network = django.ForeignKey(Network, null=True, on_delete=django.PROTECT)

    class Meta:
        abstract = True

class NetworkRelationMixin(django.Model):
 
    networks = django.ManyToManyField(Network)
 
    class Meta:
        abstract = True


class NetworkModel(NetworkMixin, ResourceModel):

    class Meta(ResourceModel.Meta):
        abstract = True
        unique_together = ('network', 'name')

    def __str__(self):
        return "{}:{}".format(self.network.name, self.name)

    def get_id_fields(self):
        return ('name', 'network_id')
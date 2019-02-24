from django.db import models as django

from data.subnet.models import Subnet
from .resource import ResourceModel, ResourceModelFacadeMixin


class SubnetModelFacadeMixin(ResourceModelFacadeMixin):

    def set_scope(self, subnet):
        super().set_scope(subnet_id = subnet.id)


class SubnetMixin(django.Model):
    
    subnet = django.ForeignKey(Subnet, null=True, on_delete=django.PROTECT)

    class Meta:
        abstract = True

class SubnetRelationMixin(django.Model):
 
    subnets = django.ManyToManyField(Subnet)
 
    class Meta:
        abstract = True


class SubnetModel(SubnetMixin, ResourceModel):

    class Meta(ResourceModel.Meta):
        abstract = True
        unique_together = ('subnet', 'name')

    def __str__(self):
        return "{}:{}".format(self.subnet.name, self.name)

    def get_id_fields(self):
        return ('name', 'subnet_id')
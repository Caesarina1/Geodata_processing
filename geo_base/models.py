from django.db import models
import uuid
from django.contrib.auth.models import User, Group, Permission, ContentType


class Target(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, editable=False)
    type = models.CharField(max_length=100, null=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    comment = models.CharField(max_length=1000, null=True)
    users = models.ManyToManyField(User, related_name='targets')


combat_units, created = Group.objects.get_or_create(name='Combat Units')
agents, created = Group.objects.get_or_create(name='Agents')

content_type = ContentType.objects.get_for_model(Target)

try:

    permissionCU = Permission.objects.create(codename='can_view_position', name='Can view position page',
                                             content_type=content_type,)
    permissionA = Permission.objects.create(codename='can_view_data_transfer', name='Can view data transfer page',
                                            content_type=content_type,)
    combat_units.permissions.add(permissionCU)
    agents.permissions.add(permissionA)

except BaseException:
    print(BaseException)

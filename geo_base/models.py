from django.db import models
# from django.contrib.gis.db import models as gis_models
import uuid
from django.contrib.auth.models import User


class Target(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=False, editable=False)
    type = models.CharField(max_length=100, null=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    comment = models.CharField(max_length=1000, null=True)
    users = models.ManyToManyField(User, related_name='targets')

    class Meta:
        permissions = (("can_view_data_transfer", "Can view data transfer page"), ("can_view_position", "Can view position page"),)

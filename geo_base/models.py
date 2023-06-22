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


# class Marker(gis_models.Model):
#     name = gis_models.CharField(max_length=255)
#     location = gis_models.PointField()
#
#     def __str__(self):
#         return self.name


# class Journal(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True, primary_key=True, editable=False)
#     user = models.
#     user_journal_rel = models.ManyToManyField(User, related_name='users')
#     target =
#     target_journal_rel = models.ManyToManyField(Target, related_name='targets')
#     comment = models.TextField(max_length=100)

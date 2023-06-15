from django.db import models
import uuid

# Create your models here.


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, editable=False)
    login = models.CharField(null=False, max_length=20)
    password = models.CharField(null=False, max_length=30)
    role = models.CharField(null=False, default='Agent')  #choices=[("agent", "Agent"), ("combat unit"), ("Сombat unit")])


class Target(models.Model):
    target_id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    type = models.CharField(max_length=100, null=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    users = models.ManyToManyField(User, related_name='targets')


# class Journal(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True, primary_key=True, editable=False)
#     user = models.
#     user_journal_rel = models.ManyToManyField(User, related_name='users')
#     target =
#     target_journal_rel = models.ManyToManyField(Target, related_name='targets')
#     comment = models.TextField(max_length=100)

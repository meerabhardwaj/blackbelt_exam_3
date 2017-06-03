from __future__ import unicode_literals

from django.db import models
from ..log_reg.models import User

# Create your models here.


class PlanManager(models.Manager):
    def create_trip(self, postData, user_id):
        pass

    def join_trip(self, id, user_id):
        pass


class Plan(models.Model):
    destination = models.CharField(max_length=48)
    description = models.TextField(max_length=1000)
    start_date = models.DateField(auto_now=False)
    end_date = models.DateField(auto_now=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    creator = models.ForeignKey(User, related_name='created_trip')
    joiners = models.ManyToManyField(User, related_name='joined_trip')

    objects = PlanManager()

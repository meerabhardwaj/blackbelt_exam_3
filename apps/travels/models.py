from __future__ import unicode_literals

from django.db import models
from ..log_reg.models import User

# Create your models here.


class PlanManager(models.Manager):
    def create_trip(self, user_id, postData):
        errors = []

        # no empty entires
        if len(postData['destination']) < 1 and len(postData['description']) < 1 and len(postData['start_date']) < 1 and len(postData['end_date']) < 1:
            errors.append('This form cannot have any empty entires!')

        # travel dates should be future-dated

        # travel end dates should be after start_date

        response_to_views = {}
        if not errors:
            trip = self.create(
                destination=postData['destination'],
                description=postData['description'],
                start_date=postData['start_date'],
                end_date=postData['end_date'],
                creator=User.objects.get(id=user_id)
            )
            trip.save()
            trip.joiners.add(User.objects.get(id=user_id))
            response_to_views['status'] = True
            response_to_views['trip'] = trip
        else:
            response_to_views['status'] = False
            response_to_views['errors'] = errors

        return response_to_views

    def join_trip(self, id, trip_id):
        response_to_views = {}
        joining_trip = Plan.objects.filter(id=trip_id)
        if joining_trip:
            joining_trip = self.get(id=trip_id).joiners.add(User.objects.get(id=id))
            response_to_views['status'] = True
        else:
            response_to_views['status'] = False
            response_to_views['errors'] = "Trip not found or joined."
        return response_to_views


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

#-*- coding: utf-8 -*-
from datetime import datetime, timedelta, time

from django.db import models
from django.core.exceptions import ValidationError, PermissionDenied
from django.utils.functional import cached_property
from django.contrib.auth.models import Group
from django.utils import timezone


from field_application.account.models import Organization
from field_application.utils.model_field import  MultiSelectField


class Room(models.Model):
    """The meeting room entity."""
    
    name = models.CharField(max_length=32)
    managers = models.ManyToManyField(Group)

    def __unicode__(self):
        return self.name

    def judge_perms(self, managers, user):
        groups = user.groups.all()
        managers_list = [str(manager) for manager in managers.all()]
       
        for group in groups:
            return bool(str(group) in managers_list)


class RoomApplication(models.Model):


    organization = models.ForeignKey(Organization)
    room  = models.ForeignKey(Room)
    date = models.DateField()

    def clean_date(self):
        date = self.date
        now = timezone.now().date()

        if date < now:  
            raise ValidationError('该日期已过')
        if date > now + timedelta(days=14):
            raise ValidationError('超过14天')
        return date  
    
    def save(self):
        pass 


class MeetingRoomApplication(RoomApplication):

    applicant_name = models.CharField(max_length=10)
    
    def save(self):

        self.clean_date()

        super(MeetingRoomApplication, self).save()


class StuRoomApplication(RoomApplication):

    applicant_number = models.CharField(max_length=10)
    
    def save(self):

        self.clean_date()

        super(StuRoomApplication, self).save()
  
     


        
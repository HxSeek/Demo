#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Organization(models.Model):

    class Meta:
        permissions = (
            ('apply', u'可以使用会议室'),
            ('manager', u'可管理所有表单'),
            ('Stone1', u'可以管理石头坞一楼'),
            ('Stone2', u'可以管理石头坞二楼'),
        )

    user = models.OneToOneField(User) 
    chinese_name = models.CharField(max_length=30, unique=True)
    org_in_charge = models.CharField(max_length=30)
    tutor = models.CharField(max_length=20)
    tutor_contact_infor = models.CharField(max_length=30)
    director = models.CharField(max_length=20)
    director_contact_infor = models.CharField(max_length=30)
    belong_to = models.CharField(max_length=10)
    is_banned = models.BooleanField(default=True)
    

        
    
        

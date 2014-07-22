#-*- coding: utf-8 -*-
from datetime import timedelta

from django import forms
from django.utils import timezone
from django.forms.extras.widgets import SelectDateWidget
from django.forms import Textarea, RadioSelect
from django.forms import CheckboxSelectMultiple 

from .models import MeetingRoomApplication 
from .models import StuRoomApplication


class MeetingRoomApplicationForm(forms.ModelForm):
    #place = forms.ChoiceField(choices=MeetingRoomApplication.PLACE,
    #                          widget=RadioSelect())
    class Meta:
        model = MeetingRoomApplication
        widgets = {
            'date': SelectDateWidget(),
        }

class StuRoomApplicationForm(forms.ModelForm):
    #place = forms.ChoiceField(choices=MeetingRoomApplication.PLACE,
    #                          widget=RadioSelect())
    class Meta:
        model = StuRoomApplication
        widgets = {
            'date': SelectDateWidget(),
        }


  

#-*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms import HiddenInput
from .models import Organization


BELONG_TO_CHOICES = (
    ('其它','其它'),
    ('社团联合会','社团联合会'),
    ('校学生会','校学生会'),
    )

class SignInForm(AuthenticationForm):
    username = forms.ModelChoiceField(queryset=User.objects.all())


class SignUpForm(UserCreationForm):

    chinese_name = forms.CharField(max_length=30)
    org_in_charge = forms.CharField(max_length=30)
    tutor = forms.CharField(max_length=20)
    tutor_contact_infor = forms.CharField(max_length=30)
    director = forms.CharField(max_length=20)
    director_contact_infor = forms.CharField(max_length=30)
    belong_to = forms.ChoiceField(choices=BELONG_TO_CHOICES)


    def save(self):
        new_user = super(SignUpForm, self).save()
        org = Organization.objects.create(
            user=new_user,
            org_in_charge=self.cleaned_data['org_in_charge'],
            tutor=self.cleaned_data['tutor'],
            tutor_contact_infor=self.cleaned_data['tutor_contact_infor'],
            director=self.cleaned_data['director'],
            director_contact_infor=self.cleaned_data['director_contact_infor'],
            belong_to=self.cleaned_data['belong_to'])
        org.save()
        return org
   


   


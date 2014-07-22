from django.conf.urls import url, patterns

from .views import ApplyRoomView, ListView
from .views import ModifyView
from .forms import MeetingRoomApplicationForm
from .forms import StuRoomApplicationForm
from .models import MeetingRoomApplication, StuRoomApplication

urlpatterns = patterns(
    '',
    url(r'^apply/mroom/$', ApplyRoomView.as_view(),
               { 'appform' : MeetingRoomApplicationForm }, name='apply1'),

    url(r'^list1/$', ListView.as_view(), 
    	       { 'model' : MeetingRoomApplication }, name='list1'),

    url(r'^modify/mroom/$', ModifyView.as_view(),
               { 'appform' : MeetingRoomApplicationForm,
                 'model' : MeetingRoomApplication }, name='modify1'),

    url(r'^apply/sturoom/$', ApplyRoomView.as_view(),
               {'appform' : StuRoomApplicationForm }, name='apply2'),

    url(r'^list2/$', ListView.as_view(), 
    	       { 'model' : StuRoomApplication }, name='list2'),

    url(r'^modify/sturoom/$', ModifyView.as_view(), 
    	       { 'appform' : StuRoomApplicationForm, 
    	         'model' : StuRoomApplication }, name='modify2'),
    )
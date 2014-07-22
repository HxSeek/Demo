#-*- coding: utf-8 -*-
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from field_application.utils.decorators import check_perms
from field_application.utils.decorators import check_ownership
from .forms import MeetingRoomApplicationForm
from .models import RoomApplication


class ApplyRoomView(View):
    
    
    @method_decorator(login_required)
    @method_decorator(check_perms('account.apply'))
    def get(self, request, appform):
         return render(request, 
                      'mroom/form.html', 
                      {'form': appform(),
                      'post_url': reverse('models:apply1')})

    @method_decorator(login_required)
    @method_decorator(check_perms('account.apply'))
    def post(self, request, appform):
        form = appform(request.POST)
        if not form.is_valid():
            return render(request, 
                      'mroom/form.html', 
                      {'form': form(),
                      'post_url': reverse('models:apply1')})
        form.save()
        return HttpResponseRedirect(reverse('home'))


class ListView(View):     
    
    def manage_list(request, model):
        app = RoomApplication.objects.all()
        paginator = Paginator(app, 6)
        page = request.GET.get('page')
     
        try:
            page = paginator.page(page)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
    
        return render(request, 'mroom/list.html', {'page': page})


class ModifyView(View):


    @method_decorator(login_required)
    @method_decorator(check_ownership(RoomApplication))
    def get(self, request, appform, model):
      app_id = request.GET.get('id')
      app = get_object_or_404(model, id=app_id)
      form = appform(instance=app)
      return render(request, 'mroom/form.html',
                    {'form': form(), 'app_id': app_id,
                    'post_url': reverse('models:modify1')+'?id='+app_id})
    
    @method_decorator(login_required)
    @method_decorator(check_ownership(RoomApplication))
    def post(self, request, appform, model):
      app_id = request.GET.get('id')
      app = get_object_or_404(model, id=app_id)
      form = appform(request.POST, instance=app)
      if not form.is_valid():
          return render(request, 'mroom/form.html', 
                {'form': form(), 'app_id': app_id, 
                'post_url': reverse('models:modify1')+'?id='+app_id})
      form.save()
      return HttpResponseRedirect(reverse('home'))
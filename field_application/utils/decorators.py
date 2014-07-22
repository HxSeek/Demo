#-*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.exceptions import ValidationError, PermissionDenied

from field_application.account.models import Organization


def check_perms(perm):
    ''' accustomed version of permission_required '''
    def decorator(function):
        def wrapped_check(request, *args, **kwargs):
            if not isinstance(perm, (list, tuple)):
                perms = (perm, )
            else:
                perms = perm
            if not request.user.has_perms(perms):
                return render(request, 'deny.html', {'message': u'you can\'t apply the room'})
            return function(request, *args, **kwargs)
        return wrapped_check
    return decorator


def check_ownership(ApplicationModel):
    ''' Check whether the application is belong to the user 
    '''
    def decorator(function):
        def wrapped_check(request, *args, **kwargs):
            app_id = request.GET.get('id')
            app = get_object_or_404(ApplicationModel, id=app_id)
            user = request.user
            if not app_id:
                return render(request, 'deny.html',
                        {'message': u'非法地址'})
            if request.user.organization.id == app.organization.id \
                    or app.room.judge_perms(app.room.managers, user):
                return function(request, *args, **kwargs)
            return render(request, 'deny.html',
                        {'message': u'不能修改他人申请表'})
        return wrapped_check
    return decorator




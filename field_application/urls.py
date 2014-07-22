from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'),
               name='home'),
    url(r'^account/', include('field_application.account.urls',
                              namespace='account')),
    url(r'^mroom/',include('field_application.models.urls',
                              namespace='models')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

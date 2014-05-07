from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'unist_tumblr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'core.views.index', name='index'),
    url(r'^home/$', 'core.views.index', name='home'),
    url(r'^about/$', 'core.views.about', name='about'),
)


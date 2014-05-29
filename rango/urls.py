from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
    url(r'^$','rango.views.index'),
    url(r'^about/$','rango.views.about'),
    url(r'^add_category/$', 'rango.views.add_category'),
    url(r'^category/(?P<category_name_url>\w+)/add_page/$','rango.views.add_page'),
    url(r'^category/(?P<category_name_url>\w+)/$', 'rango.views.category'),
    url(r'^register/$', 'rango.views.register'),
    url(r'^login/$','rango.views.user_login'),
    url(r'^logout/$','rango.views.user_logout'),
    url(r'^restricted/$', 'rango.views.restricted'),
    url(r'^search/$', 'rango.views.search'),
    url(r'^goto/$', 'rango.views.track_url', name='track_url'),
    url(r'^profile/$', 'rango.views.profile', name='profile'),
    url(r'^suggest_category/$', 'rango.views.suggest_category', name='suggest_category'),
    url(r'^auto_add_page/$', 'rango.views.auto_add_page', name='auto_add_page'),
    )


from django.conf import urls
from django.http.response import HttpResponse
from django.urls import path
from . import views


urlpatterns=[
    path('',views.homeview,name='home'),
    path('statewise',views.statewiseview,name='statewise'),    
    path('contact',views.contactview,name='contact'),   
    path('confirmed',views.confirmedview,name='confirmed'),
    path('death',views.deathview,name='death'),
    path('recovered',views.recoveredview,name='recovered'),
    path('total_confirmed',views.total_confirmedview,name='total_confirmed'),
    path('total_death',views.total_deathview,name='total_death'),
    path('total_recovered',views.totol_recoveredview,name='total_recovered'),
    path('state',views.stateview,name='state')
]

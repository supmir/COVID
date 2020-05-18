from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cc', views.cc, name='cc'),
    path('dcc', views.dcc, name='dcc'),
    path('pzc', views.pzc, name='pzc'),
    path('DearCovid', views.messages, name='messages'),
]

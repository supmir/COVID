from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('DearCovid', views.messages, name='messages'),
    path('DearCovid/<str:page>', views.messages, name='messages'),
    # path('cc', views.cc, name='cc'),
    # path('dcc', views.dcc, name='dcc'),
    # path('pzc', views.pzc, name='pzc'),
    path('<str:pagename>', views.multiview),
]

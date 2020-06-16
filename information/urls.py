from django.urls import path

from . import views
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', views.index, name='index'),
    # path('DearCovid', views.messages, name='messages'),
    path('DearCovid', RedirectView.as_view(url = "http://19-ncov.cf/DearCovid/1"), name='messages'),
    path('DearCovid/<int:page>', views.messages, name='messages'),
    # path('cc', views.cc, name='cc'),
    # path('dcc', views.dcc, name='dcc'),
    # path('pzc', views.pzc, name='pzc'),
    path('<str:pagename>', views.multiview),
]

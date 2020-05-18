from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader
# Create your views here.
from .models import Messages

def index(request):
    template = loader.get_template('information/index.html')
    context = {}
    return HttpResponse(template.render(context,request))

def cc(request):
    template = loader.get_template('information/cc.html')
    context = {}
    return HttpResponse(template.render(context,request))

def dcc(request):
    template = loader.get_template('information/dcc.html')
    context = {}
    return HttpResponse(template.render(context,request))

def pzc(request):
    template = loader.get_template('information/pzc.html')
    context = {}
    return HttpResponse(template.render(context,request))


def messages(request):
    latest_message_list = Messages.objects.order_by('-timestamp')
    context = {'latest_message_list': latest_message_list}
    return render(request, 'information/messages.html', context)

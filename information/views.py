from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader
from django.core.paginator import Paginator

# Create your views here.
from .models import Messages
import os
import math
from django.http.response import Http404

def index(request):
    template = loader.get_template('information/index.html')
    context = {}
    return HttpResponse(template.render(context,request))


def multiview(request,pagename):

    FTP_UPLOAD_DIR = '/home/iskandar_amir/covid2/static/information/html/'
    if os.path.exists(FTP_UPLOAD_DIR + pagename+".html"):
    # if yes, then serve the page
        with open(FTP_UPLOAD_DIR + pagename+".html") as f:
            response = HttpResponse(f.read())
        return response

    else:
        raise Http404
    

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


def messages(request, page=1):
    length = 24
    if(page<=0):
        page=1
    latest_message_list = Messages.objects.order_by('-timestamp')
    paginator = Paginator(latest_message_list, 20)

    page_obj = paginator.get_page(page)

    context = {'latest_message_list': latest_message_list,
                'page_obj':page_obj,
    }
    return render(request, 'information/messages.html', context)
# def messages(request, page=1):
#     if(page<0):
#         page=0
#     the_message = Messages.objects.order_by('-timestamp')[page]
#     context = {'the_message': the_message,
#                 'prev_page':page-1,
#                 'next_page':page+1 if len(latest_message_list)==length else 0,
#     }
#     return render(request, 'information/messages.html', context)

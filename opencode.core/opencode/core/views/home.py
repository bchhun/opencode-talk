#coding: utf8

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.conf import settings

def home(request):
    data = {}
    return render_to_response("accueil.html", data, context_instance=RequestContext(request))
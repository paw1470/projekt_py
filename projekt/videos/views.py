# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>videos homepage</h1>")

def detail(request, tutorial_id):
    return HttpResponse("<h2>Detale tutoriala: " +str(tutorial_id)+"</h2>")
# Create your views here.

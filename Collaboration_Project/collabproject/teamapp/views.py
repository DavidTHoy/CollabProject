from django.shortcuts import render
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse



# Create your views here.
def index(request):
    template = loader.get_template('teamapp/team-menu.html')
    context = {}
    return HttpResponse(template.render(context, request))

def assignment(request):
    template = loader.get_template('teamapp/team-assignment.html')
    context = {}
    return HttpResponse(template.render(context, request))

def members(request):
    template = loader.get_template('teamapp/team-member.html')
    context = {}
    return HttpResponse(template.render(context, request))

def score(request):
    template = loader.get_template('teamapp/team-score.html')
    context = {}
    return HttpResponse(template.render(context, request))

def topic(request):
    template = loader.get_template('teamapp/team-topic.html')
    context = {}
    return HttpResponse(template.render(context, request))
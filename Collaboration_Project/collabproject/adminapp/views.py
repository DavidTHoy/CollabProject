from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import AddMemberForm
from .models import Member


# Create your views here.
def index(request):
    template = loader.get_template('adminapp/admin-home.html')
    context = {}
    return HttpResponse(template.render(context,request))

def topic(request):
    template = loader.get_template('adminapp/admin-topic.html')
    context = {}
    return HttpResponse(template.render(context,request))

def team(request):
    template = loader.get_template('adminapp/admin-team.html')

    if request.method == 'GET':
        form = AddMemberForm()
        context = {
            "form": form
        }
        return HttpResponse(template.render(context, request))

    if request.method == 'POST':
        form = AddMemberForm(request.POST)
        if form.is_valid():

            fName = form.cleaned_data['fName']
            lName = form.cleaned_data['lName']
            location = form.cleaned_data['location']
            cec = form.cleaned_data['cec']
            member_item = form.save(commit=False)
            member_item.save()
            context = {
                "form": form,
                "fName": fName,
                "lName": lName,
                "cec": cec,
                "location": location
            }
            return HttpResponse(template.render(context, request))



def timeslot(request):
    template = loader.get_template('adminapp/admin-timeslot.html')
    context = {}
    return HttpResponse(template.render(context,request))

def assignment(request):
    template = loader.get_template('adminapp/admin-assignment.html')
    context = {}
    return HttpResponse(template.render(context,request))


from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import MemberForm


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
    form = MemberForm()
    context = {
        "form": form
    }

    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():

            fName = form.cleaned_data['fName']
            name = fName.split()
            fName = name[0]
            lName = name[1]
            cec = form.cleaned_data['cec']
            location = form.cleaned_data['location']
            form.save()
            context = {
                "form": form,
                "fName": fName,
                "lName": lName,
                "cec": cec,
                "location": location
            }
            return HttpResponse(template.render(context, request))

    #return render(request, template, context)


    return HttpResponse(template.render(context,request))

def timeslot(request):
    template = loader.get_template('adminapp/admin-timeslot.html')
    context = {}
    return HttpResponse(template.render(context,request))

def assignment(request):
    template = loader.get_template('adminapp/admin-assignment.html')
    context = {}
    return HttpResponse(template.render(context,request))


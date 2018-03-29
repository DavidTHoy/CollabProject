from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import AddMemberForm, MembersForm
from .models import Member
import random, copy

y = {}

def showTeams():
    member = Member.objects.all()

    team = [mem.fName + ' ' + mem.lName for mem in member]
    random.shuffle(team)
    temp = []

    count = 1
    print(team)
    y.clear()
    left_over = len(team) / 5
    ##print(left_over)
    for mem in team:
        # print(mem)
        # if mem % 4 == 0 and mem != 0:
        if count == 5:

            # temp.append(team[mem])
            temp.append(mem)
            y[len(y) + 1] = copy.deepcopy(temp)
            print(temp)
            ##print(len(y))
            ##print(y)
            ##print("true")
            del temp[:5]
            count = 1

        elif count < 5:
            # temp.append(team[mem])
            temp.append(mem)
            count = count + 1

            print(temp)
            ##print(len(y))
            ##print(y)
    if len(temp) < 5 and len(temp) != 0:
        y[len(y) + 1] = copy.deepcopy(temp)

def saveTeam():
    y.clear()
    print(y)

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
    member = Member.objects.all()

    if request.method == 'GET':
        form = AddMemberForm()
        memberForm = MembersForm()



        memberForm.fields['members'].choices = [(m.fName+' '+m.lName, m.fName+' '+m.lName) for m in member]
        context = {
            "form": form,
            "member": member,
            "y": y,
            "memberForm": memberForm
        }
        return HttpResponse(template.render(context, request))

    if request.method == 'POST':
        form = AddMemberForm(request.POST)

        print(form.is_valid())
        print(form.errors)
        if form.is_valid():

            fName = form.cleaned_data['fName']
            lName = form.cleaned_data['lName']
            location = form.cleaned_data['location']
            cec = form.cleaned_data['cec']
            cohort = form.cleaned_data['cohort']
            member_item = form.save(commit=False)
            member_item.save()
            form = AddMemberForm()
            memberForm = MembersForm()
            memberForm.fields['members'].choices = [(m.fName + ' ' + m.lName, m.fName + ' ' + m.lName) for m in member]
            context = {
                "form": form,
                "fName": fName,
                "lName": lName,
                "cec": cec,
                "location": location,
                "cohort":cohort,
                "memberForm": memberForm
            }

            return HttpResponse(template.render(context, request))
        else:
            context = {}
            return HttpResponse(template.render(context, request))




def createTeam(request):

    template = loader.get_template('adminapp/admin-team.html')

    if request.method == 'POST':
        if 'assignBtn' in request.POST:
            #team = request.POST.getlist('selected_member_id')
            post = request.POST
            member = Member.objects.all()
            showTeams()



            form = AddMemberForm()
            memberForm = MembersForm()



            memberForm.fields['members'].choices = [(m.fName + ' ' + m.lName, m.fName + ' ' + m.lName) for m in member]

            context = {
            'form':form,
            'memberForm':memberForm,
            'y':y
            }
        elif 'saveBtn' in request.POST:
            member = Member.objects.all()
            form = AddMemberForm()
            memberForm = MembersForm()



            memberForm.fields['members'].choices = [(m.fName + ' ' + m.lName, m.fName + ' ' + m.lName) for m in member]
            ##y.clear()
            saveTeam()
            context = {
                'form': form,
                'memberForm': memberForm,
                'y': y
            }

        else:
            team = request.POST.getlist('selected_member_id')
            post = request.POST

            form = AddMemberForm()
            memberForm = MembersForm()
            member = Member.objects.all()
            for mem in member:
                for t in team:
                    if mem.fName + ' ' + mem.lName == t:
                        member.filter(cec=mem.cec).delete()

            member = Member.objects.all()
            memberForm.fields['members'].choices = [(m.fName + ' ' + m.lName, m.fName + ' ' + m.lName) for m in member]
            print(member)

            context = {
                'form': form,
                'memberForm': memberForm
            }
            # print(x)



    return HttpResponse(template.render(context, request))


def timeslot(request):
    template = loader.get_template('adminapp/admin-timeslot.html')
    context = {}
    return HttpResponse(template.render(context,request))

def assignment(request):
    template = loader.get_template('adminapp/admin-assignment.html')
    context = {}
    return HttpResponse(template.render(context,request))


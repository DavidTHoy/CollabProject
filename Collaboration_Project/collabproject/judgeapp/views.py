from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import ChoicesForm, UserLoginForm, UserRegistrationForm, Timeslot
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template, render_to_string
from django.core.mail import send_mail

from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

)


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("index")
    template = loader.get_template('judgeapp/judge-login.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))


def register_view(request):
    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            return redirect("index")
    context = {
        'form': form
    }

    return render(request, "judgeapp/register.html", context)


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required(login_url='login')
def index(request):
    template = loader.get_template('judgeapp/judge-home.html')
    context = {}
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def score(request):
    template = loader.get_template('judgeapp/judge-score.html')
    context = {}
    return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def timeslot(request):
    template = loader.get_template('judgeapp/judge-timeslot.html')
    if request.method == 'POST':
        data = request.POST.getlist('slot')
        test = Timeslot.objects.filter(user=request.user).values_list('id', flat=True)

        form = ChoicesForm(request.POST)
        if form.is_valid():
            for eachid in test:
                t = Timeslot.objects.get(pk=eachid)
                t.user.remove(request.user)
                t.save()

            for slot in data:
                it = slot.split(" ", 1)
                t = Timeslot.objects.get(pk=it[0])
                t.user.add(request.user)
                t.save()
            request.session['entered_form_data'] = data

            return HttpResponseRedirect('results')

        else:
            return HttpResponse('not working right')
    else:
        form = ChoicesForm()
        context = {'form': form}
        return HttpResponse(template.render(context, request))


@login_required(login_url='login')
def results(request):
    template = 'judgeapp/results.html'
    chosenWID = request.session.pop('entered_form_data', None)
    current_user = request.user
    chosen = []

    for each in chosenWID:
        chose = (each.split(" ", 1))
        chosen.append(chose[1])
    # Takes stored data from form and pushes to results html
    context = {
        'chosen': chosen
    }
    send_that_mail(chosen, current_user)
    return render(request, template, context)


def send_that_mail(chosen, current_user):
    msg_plain = render_to_string('email.txt', {'chosen': chosen, 'current_user': current_user})
    msg_html = render_to_string('email.html', {'chosen': chosen, 'current_user': current_user})
    send_mail(
        'Timeslot Selection Notification',
        msg_plain,
        'ciscocrosscollab@gmail.com',
        [current_user.email],
        html_message=msg_html,
    )

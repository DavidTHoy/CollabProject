from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Member

class AddMemberForm(forms.Form):
    locations = (
        ('RTP','RTP'),
        ('Mexico', 'Mexico'),
        ('Krakow','Krakow'),
    )
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}),max_length=50)
    cec = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'CEC'}),max_length=10)
    location = forms.ChoiceField(choices=locations)

class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['fName','cec','location']
        widgets = {
            'fName': forms.TextInput(attrs={'placeholder':'Name'}),
            'cec': forms.TextInput(attrs={'placeholder':'CEC'}),
        }


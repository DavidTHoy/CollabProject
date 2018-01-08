from django import forms
from django.forms import ModelForm
from django.db import models
from .models import Member


class AddMemberForm(ModelForm):
    class Meta:
        model = Member
        fields = ['fName','lName','cec','location']
        widgets = {
            'fName': forms.TextInput(attrs={'placeholder':'First Name'}),
            'lName': forms.TextInput(attrs={'placeholder':'Last Name'}),
            'cec': forms.TextInput(attrs={'placeholder':'CEC'}),
        }
##class MembersForm(forms.Form):
    ##member = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)


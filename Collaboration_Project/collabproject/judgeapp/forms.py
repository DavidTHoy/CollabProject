from django import forms
from django.contrib.auth import(
        authenticate,
    get_user_model,
    login,
    logout,

    )
from .models import Timeslot

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("no user")

            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")

            if not user.is_active:
                raise forms.ValidationError("User is no longer active")
            return super(UserLoginForm, self).clean(*args,**kwargs)

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'email',
            'email2',
        ]
    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError("emails must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been taken")
        return email


class ChoicesForm(forms.Form):
    SELECTIONS = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=[])
    CHOICES = []

    def __init__(self, *args, **kwargs):
        super(ChoicesForm, self).__init__(*args, **kwargs)
        timeslots = Timeslot.objects.all()
        self.SELECTIONS = forms.MultipleChoiceField(choices=[tuple((slot.id, slot) for slot in timeslots)])
        self.CHOICES = list((slot.id, slot) for slot in timeslots)



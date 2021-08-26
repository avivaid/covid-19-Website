from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class dateForm(forms.Form):
    date = forms.CharField(
        label = "Enter date in m/dd/yy ",
        required = False,
        max_length = 30, 
    )    
class fullDateForm(forms.Form):
    date = forms.CharField(
        label = "Enter date in yyyy-mm-dd ",
        required = False,
        max_length = 30, 
    )    
class stateForm(forms.Form):
    state = forms.CharField(
        label = "Enter the State/Country",
        required = False,
        max_length = 30, 
    )    
 
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True,
        )

    class Meta:
        model = User
        fields = ("username", "email",
                  "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
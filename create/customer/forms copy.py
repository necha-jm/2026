from django import forms
from .models import Loginmodel

class LoginForm(forms.Form):
    model = Loginmodel
    fields = ['Firstname','Lastname','phoneNumber']
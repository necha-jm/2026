from django import forms
from .models import Loginmodel

# class Loggingin(forms.ModelForm):
#     password1 = forms.CharField()

#     class Meta:
#         model = Loginmodel
#         fields = ['username','Firstname','Lastname','phoneNumber']
           
#         widgets = {
#                'password1':
#                forms.PasswordInput()
#            }

class Loggingin(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'login__input', 'placeholder': 'Password'}))

    class Meta:
        model = Loginmodel
        fields = ['username', 'Firstname', 'Lastname', 'phoneNumber', 'password1']
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'User name / Email'}),
            'Firstname': forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'First Name'}),
            'Lastname': forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'Last Name'}),
            'phoneNumber': forms.TextInput(attrs={'class': 'login__input', 'placeholder': 'Phone Number'}),
        }

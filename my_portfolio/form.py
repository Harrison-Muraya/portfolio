from django.forms import ModelForm
from . models import User
from django import forms


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','firstname','lastname','email','contact')
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            
        }




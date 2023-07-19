from django.forms import ModelForm
from . models import Users
from django import forms


class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ('firstname','lastname','email','contact')
        
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            
        }




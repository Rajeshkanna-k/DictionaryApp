from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Word, Visitor

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')

class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = ('name','is_found')
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Enter the word'})}

class VisitorsForm(ModelForm):
    class Meta:
        model = Visitor
        fields = ('visitors_count', 'created_date')
        

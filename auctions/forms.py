from django import forms
from .models import Carousel,User
from django.core.validators import EmailValidator
from django.contrib.auth.forms import UserCreationForm as BaseUserCreationForm

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(validators=[EmailValidator()])
    phone = forms.CharField(max_length=15)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

class CarouselModelForm(forms.ModelForm):
    class Meta:
        model=Carousel
        fields=[
           'title',
           'cover_image',
            'status',
       ]

class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','age', 'password1', 'password2','phone','code','adres')

class VerifyForm(forms.Form):
    code = forms.CharField(max_length=8, required=True, help_text='Enter code')
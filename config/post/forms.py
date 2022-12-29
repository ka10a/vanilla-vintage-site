from django import forms
from django.forms import ModelForm, DateInput
from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Full Name',
        'class': 'form-control'
    }))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'placeholder': 'E-mail Address',
        'class': 'form-control'
    }))
    address = forms.CharField(label='', max_length=300, widget=forms.TextInput(attrs={
        'placeholder': 'Physical Address',
        'class': 'form-control'
    }))
    ids = forms.CharField(label='', max_length=1000, widget=forms.TextInput(attrs={
        'placeholder': 'Put IDs of products you want to buy or reserve for us to contact with you on',
        'class': 'form-control'
    }))


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Full Name',
        'class': 'form-control'
    }))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'placeholder': 'E-mail Address',
        'class': 'form-control'
    }))
    subj = forms.CharField(label='', max_length=300, widget=forms.TextInput(attrs={
        'placeholder': 'Subject',
        'class': 'form-control'
    }))
    text = forms.CharField(label='', max_length=1000, widget=forms.TextInput(attrs={
        'placeholder': 'Your Message',
        'class': 'form-control'
    }))
from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Name'}), label='')
    email = forms.EmailField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Email'}), label='')
    subject = forms.CharField(max_length=30, required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Subject'}), label='')

    message = forms.CharField(max_length=200, required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Message'}), label='')

    class Meta:
        model = t_contact
        fields = ["name",  "email", "subject", "message"]

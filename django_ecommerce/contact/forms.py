# contact/forms.py

from django.forms import ModelForm
from .models import ContactForm
from django import forms


class ContactView(ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    form_name = 'contact_form'
    ng_scope_prefix = 'contactform'

    class Meta:
        fields = ['name', 'email', 'topic', 'message']
        model = ContactForm

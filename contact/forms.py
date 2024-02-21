from django import forms

from contact.models import Contact, NewsLetter


class contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'

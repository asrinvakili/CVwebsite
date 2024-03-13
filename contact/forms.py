from django import forms
from captcha.fields import CaptchaField
from contact.models import Contact, NewsLetter


class contact_form(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'

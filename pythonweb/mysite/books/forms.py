from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=20)
    email = forms.EmailField(required=False)
    message = forms.CharField(max_length=200, widget=forms.Textarea)
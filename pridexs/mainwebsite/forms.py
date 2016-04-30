from django import forms

class EmailForm(forms.Form):
    c_name = forms.CharField(label="Name", max_length=100)
    c_email = forms.EmailField()
    c_subject = forms.CharField(label="Subject", max_length=100)
    c_message = forms.CharField(widget=forms.Textarea)

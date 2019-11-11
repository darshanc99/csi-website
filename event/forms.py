from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label = 'name', max_length = 200)
    email = forms.EmailField(label = 'email' , max_length = 200)
    message = forms.CharField(label = 'message', widget=forms.Textarea)
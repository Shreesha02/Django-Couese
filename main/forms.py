from django import forms
from django.core.validators import RegexValidator

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone_no = forms.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    

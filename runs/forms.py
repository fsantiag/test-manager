from django import forms
from .models import Run


class RunForm(forms.Form):
    your_name = forms.CharField(
            label='Your name',
            max_length=100,
            widget=forms.TextInput(attrs={'class' : 'col-lg-4'})
            )

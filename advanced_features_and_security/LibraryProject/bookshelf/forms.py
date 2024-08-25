from django import forms
from .models import Book 

class ExampleForm(forms.Form):
    query = forms.CharField(max_length=100, required=True, label='Search Query')

  

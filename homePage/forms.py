from django import forms
from homePage.models import Tasklist

class Task(forms.ModelForm):
    class Meta:
        model = Tasklist
        fields = ['task','done']
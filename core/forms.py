from django import forms
from .models import *


class Employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'join_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class': 'form-control mb-3', 'placeholder': 'Select a date', 'type': 'date'}),
            'salary': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
            'picture': forms.FileInput(attrs={'class': 'form-control mb-3'}),
        }

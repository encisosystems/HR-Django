from tabnanny import verbose
from tkinter import Widget
from django import forms
from django.core.exceptions import ValidationError

from .models import JobDescription, Recruitment

class AddJobDescriptionForm(forms.Form):
    """ Form creation - AddJobDescription Form """

    createdBy = forms.CharField(
        label = 'Created By',
        max_length = 250,
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    creationDate = forms.CharField(
        label = 'Creation Date',
        max_length = 50,
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    code = forms.CharField(
        label = 'Code',
        max_length = 50,
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    title = forms.CharField(
        label = 'Title',
        max_length = 50,
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    departament = forms.CharField(
        label = 'Departament',
        max_length = 250,
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    reportTo = forms.CharField(
        label = 'Report To',
        max_length = 50,
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    jobDescription = forms.CharField(
        label = 'Job Description',
        max_length = 500,
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    responsabilities = forms.CharField(
        label = 'Responsabilities',
        max_length = 50,
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    skills = forms.CharField(
        label = 'Skills',
        max_length = 50,
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    abilities = forms.CharField(
        label = 'Abilities',
        max_length = 50,
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    experience = forms.CharField(
        label = 'Experience',
        max_length = 50,
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    educationRequirements = forms.CharField(
        label = 'Education Requirements',
        max_length = 50,
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    knowledge = forms.CharField(
        label = 'Knowledge',
        max_length = 50,
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    annualSalary = forms.CharField(
        label = 'Annual Salary',
        max_length = 11,
        required = True,
        widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ""})
    )

class AddRecruitmentForm(forms.Form):
    """ Form creation - AddRecruitment Form """
    
    requester = forms.CharField(
        label = 'Requester',
        max_length = 100,
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    dateOfRequest = forms.CharField(
        label = 'Date Of Request',
        max_length = 50,
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    startingDate = forms.CharField(
        label = 'Starting Date',
        max_length = 50,
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    departament_req = forms.CharField(
        label = 'Departament',
        max_length = 250,
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    jobDescription = forms.CharField(
        label = 'Job Description',
        max_length = 50,
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    numberOfVacancies = forms.CharField(
        label = 'Number Of Vacancies',
        max_length = 3,
        required = True,
        widget = forms.NumberInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    title_req = forms.CharField(
        label = 'Title',
        max_length = 250,
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    responsabilities = forms.CharField(
        label = 'Responsabilities',
        max_length = 50,
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    location = forms.CharField(
        label = 'Location',
        max_length = 250,
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
    comments = forms.CharField(
        label = 'Comments',
        max_length = 50,
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': ""})
    )
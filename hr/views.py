from django.http import request
from django.shortcuts import reverse, redirect, render
from django.views import generic
from django.conf import settings 

from hr.forms import AddJobDescriptionForm, AddRecruitmentForm
from hr.models import JobDescription, Recruitment


class RecruitmentView(generic.FormView):
    """
    The backend of the Recruitment template is implemented in this view.
    Display an individual :model:`hr.Recruitment`.
    **Template:**
    :template:`hr/recruitmentRequest.html`
    **get_success_url()**
    We return/render the template under the alias we passed as parameter.
    **form_valid()**
    Validate the form fields and save the changes.
    """
    form_class = AddRecruitmentForm
    template_name = "recruitmentRequest.html"

    def get_success_url(self):
        return reverse('hr:recruitment')

    def form_valid(self, form):
        recruitment = form.save(commit=True)
        user = self.request.user
        form.instance.user = user
        form.save()
        return super(RecruitmentView, self).form_valid(form)

class JobDescriptionView(generic.FormView):
    """
    The backend of the JobDescription template is implemented in this view.
    Display an individual :model:`hr.JobDescription`.
    **Template:**
    :template:`hr/jobDescription.html`
    **get_success_url()**
    We return/render the template under the alias we passed as parameter.
    **form_valid()**
    Validate the form fields and save the changes.
    """

    form_class = AddJobDescriptionForm
    template_name = "jobDescription.html"

    def get_success_url(self):
        return reverse('hr:jobDescription')

    def form_valid(self, form):
        job = form.save(commit=True)
        user = self.request.user
        form.instance.user = user
        form.save()
        return super(JobDescriptionView, self).form_valid(form)

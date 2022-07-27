from django.http import request
from django.shortcuts import reverse, redirect, render
from django.views import generic
from django.conf import settings 

from hr.forms import AddJobDescriptionForm, AddRecruitmentForm
from hr.models import JobDescription, Recruitment, Area


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
        recruitment = Recruitment()
        recruitment.requester = form.cleaned_data['requester']
        recruitment.departament = '1'
        recruitment.departament_req = form.cleaned_data['departament_req']
        recruitment.numberOfVacancies = form.cleaned_data['numberOfVacancies']
        recruitment.title_req = form.cleaned_data['title_req']
        recruitment.location = form.cleaned_data['location']
        recruitment.save()
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
        jobDescription = JobDescription()
        jobDescription.createdBy = form.cleaned_data['createdBy']
        jobDescription.title = form.cleaned_data['title']
        jobDescription.departament = Area.objects.get(id=form.cleaned_data['departament'])
        jobDescription.jobDescription = form.cleaned_data['jobDescription']
        jobDescription.annualSalary = form.cleaned_data['annualSalary']
        jobDescription.save()
        return super(JobDescriptionView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(JobDescriptionView, self).get_context_data(**kwargs)
        context['areas'] = Area.objects.all()
        return context

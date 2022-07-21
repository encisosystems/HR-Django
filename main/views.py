from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic


class Home(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, *args,**kwargs):

        context = super(Home, self).get_context_data(**kwargs)
        return context
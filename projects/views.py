from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from .models import Project
from .forms import ProjectForm

# Create your views here.
class ProjectListView(ListView):
	model = Project
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['latest_project'] = Project.objects.latest('created_date')
		return context
		

class ProjectDetailView(DetailView):
	model = Project

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['latest_project'] = Project.objects.latest('created_date')
		return context

class CreateProjectView(CreateView):
	model = Project
	form_class = ProjectForm
	template_name = "projects/form.html"
	success_url = reverse_lazy("project-list")
	
class HomeView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['object_list'] = Project.objects.all()
		context['latest_project'] = Project.objects.latest('created_date')
		return context
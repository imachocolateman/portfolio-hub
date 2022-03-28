from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from .models import Project
from .forms import ProjectForm

# Create your views here.
class ProjectListView(ListView):
	model = Project

class ProjectDetailView(DetailView):
	model = Project

class CreateProjectView(CreateView):
	model = Project
	form_class = ProjectForm
	template_name = "projects/form.html"
	success_url = reverse_lazy("project-list")

class HomeView(TemplateView):
	template_name = "home.html"
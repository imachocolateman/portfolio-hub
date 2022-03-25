from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Project

# Create your views here.
class ProjectListView(ListView):
	model = Project


class ProjectDetailView(DetailView):
	model = Project
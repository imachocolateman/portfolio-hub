from django.urls import path

from . views import ProjectListView, ProjectDetailView, CreateProjectView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('new/', CreateProjectView.as_view(), name="project-new"),
    path('<slug:slug>/', ProjectDetailView.as_view(), name='project-detail'),
]

from django.urls import path

from . views import ProjectListView, ProjectDetailView, CreateProjectView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('new/', CreateProjectView.as_view(), name="new-project"),
    path('<slug:slug>-proj/', ProjectDetailView.as_view(), name='project-detail'),
]

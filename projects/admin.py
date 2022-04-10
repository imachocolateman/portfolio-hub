from django.contrib import admin

from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
	list_display = ("title", "summary", "created_date", "last_updated")
	prepopulated_fields = {
		"slug": ("title",)
	}
	ordering = ['-created_date']

admin.site.register(Project, ProjectAdmin)
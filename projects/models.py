from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=100)
	summary = models.CharField(max_length=255, help_text="Please enter a short summary for the project.")
	body = models.TextField()

	PRODUCTION = 'P'
	DEVELOPMNENT = 'D'
	ABANDONED = 'X'
	RESEARCH = "R"
	STATUS_CHOICES = [
		(PRODUCTION, 'Production'),
		(DEVELOPMNENT, 'Development'),
		(ABANDONED, 'Abandoned'),
		(RESEARCH, 'Research'),
	]
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=RESEARCH)

	created_date = models.DateField(auto_now_add=True, editable=False)
	last_updated = models.DateTimeField(auto_now=True, editable=False)

	project_start_date = models.DateField(auto_now_add=True)
	project_end_date = models.DateField(blank=True)
	tag = TaggableManager()
	bg_image = models.URLField()
	external_url = models.URLField()

	def __str__(self):
		return f"{self.id} | {self.title}"


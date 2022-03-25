from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from taggit.managers import TaggableManager

# Create your models here.
def project_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'project_{instance.slug}/{filename}'

class Project(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(null=False, unique=True)
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

	project_start_date = models.DateField()
	project_end_date = models.DateField(blank=True)

	tag = TaggableManager()
	bg_image = models.ImageField(upload_to=project_directory_path)
	external_url = models.URLField(null=True)

	def __str__(self):
		return f"{self.id} | {self.title}"

	def get_absolute_url(self):
		return reverse('project-detail', kwargs={"slug": self.slug})

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)


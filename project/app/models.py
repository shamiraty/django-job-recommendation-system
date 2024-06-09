from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    image = models.ImageField(upload_to='job_images', null=True, blank=True)
    created_date = models.DateField(default=timezone.now)  # Current date auto
    deadline = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    requirements = models.TextField()
    responsibilities = models.TextField()
    contact_email = models.EmailField()
    required_skills = models.TextField()  # Required skills field
    education_level = models.CharField(max_length=255)  # Education level field

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"




from django.db import models

# Create your models here.


class campaign(models.Model):
    name = models.CharField(max_length=100)
    
    description = models.TextField()

    def __str__(self):
        return self.name



class note(models.Model):
    campaign = models.ForeignKey(campaign, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    VISIBILITY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='private')

    def __str__(self):
        return self.title
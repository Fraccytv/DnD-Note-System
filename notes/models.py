from django.db import models
from datetime import datetime

# Create your models here.


class Campaign(models.Model):
    ## Information om Campaign
    name = models.CharField(max_length=100)
    description = models.TextField()

    ## Ejerskab af Campaign
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    ## Members af Campaign
    members = models.ManyToManyField("auth.User", related_name="campaigns", blank=True)

    ## Tidsstempel for oprettelse og opdatering
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    ## Information om Note
    campaign = models.ForeignKey(
        Campaign, on_delete=models.CASCADE, related_name="notes"
    )
    title = models.CharField(max_length=100)
    content = models.TextField()

    ## Ejerskab af Note
    created_by = models.ForeignKey(
        "auth.User", on_delete=models.CASCADE, related_name="notes"
    )

    ## Tidsstempel for oprettelse og opdatering
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    ### Visibility of Note
    VISIBILITY_CHOICES = [
        ("public", "Public"),
        ("private", "Private"),
    ]
    visibility = models.CharField(
        max_length=10, choices=VISIBILITY_CHOICES, default="private"
    )

    def __str__(self):
        return self.title

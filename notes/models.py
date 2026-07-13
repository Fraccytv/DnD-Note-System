from django.db import models
from datetime import datetime
from django.utils.text import slugify

# Create your models here.


class Campaign(models.Model):
    ## Information om Campaign
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    ## Ejerskab af Campaign
    created_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    ## Members af Campaign
    members = models.ManyToManyField("auth.User", related_name="campaigns", blank=True)

    ## Tidsstempel for oprettelse og opdatering
    # created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 2

            while Campaign.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

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

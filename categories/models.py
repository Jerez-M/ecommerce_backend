from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        help_text="name should be in singular form",
    )
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
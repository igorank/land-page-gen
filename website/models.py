from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone
from uuid import uuid4


# Create your models here.

class Website(models.Model):
    # Standard Variables
    section1Title = models.CharField(null=True, blank=True, max_length=200)
    section1Description = models.TextField(null=True, blank=True)
    callToAction = models.CharField(null=True, blank=True, max_length=100)
    section1Image = models.ImageField(default='default.jpg', upload_to='landing_page_images')

    # Utility Variable
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.section1Title, self.uniqueId)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]

        self.slug = slugify()
        self.last_updated = timezone.localtime(timezone.now())
        super(Website, self).save(*args, **kwargs)


# class WebsiteService(models.Model):
#
#
# class WebsiteFeatures(models.Model):
#

from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Project(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.TextField(max_length=255)
    address = models.URLField(blank=True)
    github = models.URLField(blank=True)
    tags = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='uploads/portfolio/project_images', blank=True)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

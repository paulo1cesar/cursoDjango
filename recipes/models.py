from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    name = models.CharField(max_length=20)

class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    serving = models.IntegerField()
    serving_unit = models.CharField(max_length=65)
    preparation_step = models.TextField()
    preparation_step_is_html = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/cover/%Y/%m/%d')
    categoria = models.ForeignKey(category, on_delete=models.SET_NULL, null=True)
    categoria = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

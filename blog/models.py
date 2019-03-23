from django.db import models

# Create your models here.
# Post
# title => str
# content => long text
# author => Model
# created_at => date
# published_at => date
# published => booleen
# category => relation
class Category(models.Model):
  name = models.CharField(max_length=50)

  class Meta:
    verbose_name_plural = "categories"
  def __str__(self):
    return self.name

class Post(models.Model):
  title         = models.CharField(max_length=150)
  content       = models.TextField(blank=True)
  author        = models.ForeignKey('auth.User', models.SET_NULL, null=True)
  created_at    = models.DateTimeField(auto_now_add=True)
  publiahed_at  = models.DateTimeField(auto_now_add=False, null=True, blank=True)
  publiahed     = models.BooleanField(default=False)
  category      = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

  




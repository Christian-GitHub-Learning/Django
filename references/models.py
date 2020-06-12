from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

class ObjectManager(models.Manager):
    def get_queryset(self):
     return super().get_queryset()

class Reference(models.Model):
   
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'description')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    link = models.URLField(max_length=250)
    
    objects = models.Manager()
    referencelist = ObjectManager()

    def __str__(self):
        return self.title
        

    def get_absolute_url(self):
        return reverse_lazy('reference:reference_detail', kwargs={'pk':self.id})
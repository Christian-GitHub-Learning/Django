from django.contrib import admin

from .models import Reference

# Register your models here.

@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('id','author','title', 'body','description','link','created','updated')
    list_filter = ('title','link')
    search_fields = ('title','link')

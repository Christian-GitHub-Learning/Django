from django import template
from ..models import Reference

register = template.Library()

@register.simple_tag()
def remaining_references():
    return  Reference.referencelist.all().count()

@register.inclusion_tag('references/total_created.html')
def total_references_created():
    total_references_created = Reference.referencelist.all().order_by('-id')[:1]
    return  {'total_references_created' : total_references_created}

@register.inclusion_tag('references/latest_references.html')
def show_latest_references(count=2):
    latest_references = Reference.referencelist.all().order_by('id')[:count]
    return {'latest_references' : latest_references}

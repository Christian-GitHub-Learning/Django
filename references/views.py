from django.shortcuts import render, get_object_or_404
from .models import Reference
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.contrib.postgres.search import (SearchVector, SearchQuery, SearchRank)
#from .forms import SearchForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# def reference_list(request):

#     references = Reference.get_all(super)

#     return render(request, 'reference/list.html', {'references':reference,})


class ReferenceListView(LoginRequiredMixin, ListView):

    queryset = Reference.referencelist.all().order_by('-id')
    print(queryset)
    ##bikin kluarin query set setengah mati
    context_object_name = 'references'
    paginate_by = 5
    template_name = 'references/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def reference_detail(request):
        reference = get_object_or_404(reference)
        return reference
# Create your views here.


class ReferenceCreateView(LoginRequiredMixin, CreateView):
    model = Reference
    fields = ['title', 'description', 'body', 'link']
    template_name ='references/reference_form.html'
    success_url = reverse_lazy('references:reference_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        
        return super().form_valid(form)

class ReferenceUpdateView(LoginRequiredMixin, UpdateView):
    model = Reference
    fields = ['title', 'description', 'body', 'link']
    template_name ='references/reference_form.html'
    success_url = reverse_lazy('references:reference_list')

    def get_queryset(self):
        qs = super().get_queryset()

        return qs.filter(author = self.request.user)

    def form_valid(self, form):
        return super().form_valid(form)

class ReferenceDeleteView(LoginRequiredMixin, DeleteView):
    model = Reference
    template_name = 'references/reference_confirm_delete.html'
    success_url = reverse_lazy('references:reference_list')

    def get_queryset(self):
        qs = super().get_queryset()

        return qs.filter(author = self.request.user)
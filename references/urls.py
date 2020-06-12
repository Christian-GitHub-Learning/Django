from django.urls import path
from . import views

app_name = 'references'
urlpatterns = [
    path('',views.ReferenceListView.as_view(), name = 'reference_list'),
    path('add/',views.ReferenceCreateView.as_view(), name = 'reference_create'),
    path('update/<int:pk>/',views.ReferenceUpdateView.as_view(), name = 'reference_update'),
    path('delete/<int:pk>/',views.ReferenceDeleteView.as_view(), name = 'reference_delete'),
]
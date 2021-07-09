from Petstagram.pets.views import pet_create, pet_edit, pet_delete
from django.urls import path
from .views import pet_all, pet_details, pet_like


urlpatterns = [
    path('', pet_all, name='pet list'),
    path('details/<int:pk>', pet_details, name='pet details'),
    path('like/<int:pk>', pet_like, name='pet like'),
    path('create', pet_create, name='pet create'),
    path('edit/<int:pk>', pet_edit, name='pet edit'),
    path('delete/<int:pk>', pet_delete, name='pet delete'),
]
from .views import pet_create, pet_edit, pet_delete, pet_detail
from django.urls import path
from .views import pet_all, pet_like


urlpatterns = [
    path('', pet_all, name='pet list'),
    path('detail/<int:pk>', pet_detail, name='pet detail'),
    path('like/<int:pk>', pet_like, name='pet like'),
    path('create/', pet_create, name='pet create'),
    path('edit/<int:pk>', pet_edit, name='pet edit'),
    path('delete/<int:pk>', pet_delete, name='pet delete'),
]
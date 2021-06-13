from django.urls import path
from .views import pet_like, pet_all, pet_details


urlpatterns = [
    path('', pet_all, name='all pets'),
    path('details/<int:pk>', pet_details, name='pet details'),
    path('like/<int:pk>', pet_like, name='pet like'),
]
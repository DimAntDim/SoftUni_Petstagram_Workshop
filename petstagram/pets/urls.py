from django.urls import path
from .views import pet_all, pet_details, pet_like


urlpatterns = [
    path('', pet_all, name='pet list'),
    path('details/<int:pk>', pet_details, name='pet details'),
    path('like/<int:pk>', pet_like, name='pet like'),
]
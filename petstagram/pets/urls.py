from django.urls import path
from django.urls.conf import include
from .views import pet_all, pet_detail


urlpatterns = [
    path('', pet_all),
    path('details/<int:pk>', pet_detail)
]
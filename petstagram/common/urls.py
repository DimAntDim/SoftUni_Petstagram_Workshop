from django.urls import path
from django.urls.conf import include
from .views import landing_page

urlpatterns = [
    path('', landing_page, name='index'),
]
from accounts.views import user_login
from django.urls import path


urlpatterns = [
    path('signin/', user_login, name='user login'),
]
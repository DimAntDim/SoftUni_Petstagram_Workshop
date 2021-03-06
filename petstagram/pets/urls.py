from django.urls import path
from petstagram.pets.models import Like

from petstagram.pets.views import PetDetailsView, CommentPetView, ListPetsView, \
    CreatePetView, EditPetView, DeletePetView, pet_like

urlpatterns = [
    path('', ListPetsView.as_view(), name='list pets'),
    path('details/<int:pk>', PetDetailsView.as_view(), name='pet details'),
    path('like/<int:pk>', pet_like, name='like pet'),
    path('create/', CreatePetView.as_view(), name='create pet'),
    path('edit/<int:pk>', EditPetView.as_view(), name='edit pet'),
    path('delete/<int:pk>', DeletePetView.as_view(), name='delete pet'),
    path('comment/<int:pk>', CommentPetView.as_view(), name='comment pet'),
]

from pets.models import Pets, Like
from django.shortcuts import render

def pet_all(request):
    pets = Pets.objects.all()
    likes = Like.objects.all()
    return render(request, 'pets/pet_list.html', {
        'pets': pets,
        'likes': likes,
        })

def pet_detail(request):
    return render(request, 'pets/pet_detail.html')

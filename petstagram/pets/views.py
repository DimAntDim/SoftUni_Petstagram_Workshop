from .models import Like, Pet
from django.shortcuts import redirect, render


def pet_all(request):
    pets = Pet.objects.all()
    context = {
        'pets': pets,
    }
    return render(request, 'pets/pet_list.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    likes = Like.objects.all()
    context = {
        'pet':pet,
        'likes': len(likes),
    }
    return render(request, 'pets/pet_detail.html', context)


def pet_like(request, pk):
    pet_to_like = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet_to_like,
    )
    like.save()
    return redirect('pet details', pet_to_like.id)

def pet_create(request):
    pass

def pet_edit(request, pk):
    pass

def pet_delete(request, pk):
    pass
from pets.models import Pet, Like
from django.shortcuts import redirect, render

def pet_all(request):
    pets = Pet.objects.all()
    likes = Like.objects.all()
    return render(request, 'pets/pet_list.html', {
        'pets': pets,
        'likes': likes,
        })

def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.like_count = pet.like_set.count() # monkey typing
    context = {
        'pet': pet,
    }
    return render(request, 'pets/pet_detail.html', context)


def pet_like(request, pk):
    pet_to_like = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet_to_like,
    )
    like.save()
    return redirect('pet details', pet_to_like.id)
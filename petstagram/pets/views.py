from .forms import CreatePetForm
from .models import Like, Pet
from django.shortcuts import redirect, render


def pet_all(request):
    pets = Pet.objects.all()
    context = {
        'pets': pets,
    }
    return render(request, 'pets/pet_list.html', context)


def pet_detail(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()
    context = {
        'pet':pet,
    }
    return render(request, 'pets/pet_detail.html', context)


def pet_like(request, pk):
    pet_to_like = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet_to_like,
    )
    like.save()
    return redirect('pet detail', pet_to_like.id)

def pet_create(request):
    if request.method == 'POST':
        form = CreatePetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet list')
    form = CreatePetForm()
    context = {
        'form':form
        }
    return render(request, 'pets/pet_create.html', context)

def pet_edit(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = CreatePetForm(initial=pet)
    if form.is_valid():
        form.save()
        return redirect('pet detail')

def pet_delete(request, pk):
    pass
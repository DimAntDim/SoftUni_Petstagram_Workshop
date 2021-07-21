from .forms import CommentForm, CreatePetForm
from .models import Comment, Like, Pet
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
        'pet': pet,
        'comment_form': CommentForm(),
        'comments': pet.comment_set.all(),
    }

    return render(request, 'pets/pet_detail.html', context)


def pet_comment(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = Comment(
            text=form.cleaned_data['text'],
            pet=pet,
        )
        comment.save()
    return redirect('pet detail', pet.id)


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
    if request.method == 'POST':
        form = CreatePetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet detail', pk=pk)
    form = CreatePetForm(initial=pet.__dict__)
    return render(request, 'pets/pet_edit.html', {'form':form})

def pet_delete(request, pk):
    pet_to_delete = Pet.objects.get(pk=pk)
    if request.method == 'POST':
        pet_to_delete.delete()
        return redirect('pet list')

    context = {
        'pet':pet_to_delete
    }
    return render(request, 'pets/pet_delete.html', context)

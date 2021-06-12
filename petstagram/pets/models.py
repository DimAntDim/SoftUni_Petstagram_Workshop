from django.db import models
from django.db.models.deletion import DO_NOTHING


class Pets(models.Model):
    type_choices = (
     ("cat", "Cat"),
     ("dog", "Dog"),
     ("parrot", "Parrot"),
    )

    type = models.CharField(max_length=6, choices=type_choices)
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    image_url = models.URLField()


class Like(models.Model):
    pet = models.ForeignKey(Pets, on_delete=models.CASCADE)

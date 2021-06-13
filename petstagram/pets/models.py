from django.db import models
from django.db.models.deletion import DO_NOTHING


class Pet(models.Model):
    type_choices = (
     ("Cat", "cat"),
     ("Dog", "dog"),
     ("Parrot", "parrot"),
    )

    type = models.CharField(max_length=6, choices=type_choices)
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    image_url = models.URLField()

    def __str__(self):
        return self.name

class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    
from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

class Pet(models.Model):
    CHOICES = (
        ('Cat', 'cat'),
        ('Dog', 'dog'),
        ('Parrot', 'parrot'),
    )
    type = models.CharField(
        max_length=6, 
        choices=CHOICES
        )
    name = models.CharField(
        max_length=10,
        )
    age = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='pets/', null=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)

    def __srt__(self):
        return self.name

class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=True)

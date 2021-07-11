from django.db import models


class Pet(models.Model):
    CHOICES = (
        ('Cat', 'cat'),
        ('Dog', 'dog'),
        ('Parrot', 'parrot'),
    )
    type = models.CharField(max_length=6, choices=CHOICES)
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)

    def __srt__(self):
        return self.name

class Like(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    text = models.TextField(blank=True)

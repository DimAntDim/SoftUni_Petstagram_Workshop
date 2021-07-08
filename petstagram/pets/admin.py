from .models import Like, Pet
from django.contrib import admin


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass

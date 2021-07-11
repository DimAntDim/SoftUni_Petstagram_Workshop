from .models import Comment, Like, Pet
from django.contrib import admin


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    pass
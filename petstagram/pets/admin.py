from pets.models import Like, Pet
from django.contrib import admin


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'type', 'likes_count')

    def likes_count(self, obj):
        return obj.like_set.count()

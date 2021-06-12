from pets.models import Like, Pets
from django.contrib import admin


@admin.register(Pets, Like)
class PersAdmin(admin.ModelAdmin):
    pass



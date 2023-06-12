from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    model = Exercise
    list_display = ['name', 'exercise_type']

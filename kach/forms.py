from django import forms
from .models import *
from django.forms import formset_factory


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'slug', 'description', 'exercise_type']


class ExerciseTypeForm(forms.ModelForm):
    class Meta:
        model = ExerciseType
        fields = ['name', 'slug']


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'date', 'comment']


class SetForm(forms.ModelForm):
    exercise = forms.ModelChoiceField(queryset=Exercise.objects.all())

    class Meta:
        model = Set
        fields = ['exercise', 'repetitions', 'weight']

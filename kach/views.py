from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import *
from .forms import *


def main(request):
    # exercises = Exercise.objects.all()
    return render(request, 'kach/main.html')


# def exercise_list(request):
#     exercises = Exercise.objects.all()
#     return render(request, 'kach/exercise_list.html', {'exercises': exercises})

class ExerciseListView(ListView):
    template_name = 'kach/exercise_list.html'
    model = Exercise
    context_object_name = 'exercises'
    # queryset =


def exercise_detail(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    return render(request, 'kach/exercise_detail.html', {'exercise': exercise})


def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'kach/workout_list.html', {'workouts': workouts})


def workout_detail(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    return render(request, 'kach/workout_detail.html', {'workout': workout})


def create_exercise(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = ExerciseForm()

    return render(request, 'kach/create_exercise.html', {'form': form})


def create_exercise_type(request):
    if request.method == 'POST':
        form = ExerciseTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')  # exercise_type_list
    else:
        form = ExerciseTypeForm()

    return render(request, 'kach/create_exercise_type.html', {'form': form})


def create_workout(request):
    exercise_choices = Exercise.objects.all()
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save()  # Сохранение тренировки
            exercises = request.POST.getlist('exercises')
            repetitions = request.POST.getlist('repetitions')
            weights = request.POST.getlist('weights')
            for exercise, reps, weight in zip(exercises, repetitions, weights):
                print(exercise)
                exercise_obj = Exercise.objects.get(pk=int(exercise))
                Set.objects.create(workout=workout, exercise=exercise_obj, repetitions=reps, weight=weight)
            return redirect('main')  # Перенаправление на страницу со списком тренировок
    else:
        form = WorkoutForm()
    return render(request, 'kach/create_workout.html', {'form': form, 'exercise_choices': exercise_choices})


def update_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, pk=exercise_id)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect('exercise_list')
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, 'kach/update_exercise.html', {'form': form})

# def update_workout(request, workout_id):
#     workout = get_object_or_404(Workout, pk=workout_id)
#     if request.method == 'POST':
#         form = WorkoutForm(request.POST, instance=workout)
#         if form.is_valid():
#             form.save()
#             return redirect('workout_list')
#     else:
#         form = WorkoutForm(instance=workout)
#     return render(request, 'kach/update_workout.html', {'form': form})

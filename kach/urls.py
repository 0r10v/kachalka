"""
URL configuration for kachalka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('exercise/create/', views.create_exercise, name='create_exercise'),
    path('exercise_type/create/', views.create_exercise_type, name='create_exercise_type'),
    path('workout/create/', views.create_workout, name='create_workout'),
    path('exercise/', views.ExerciseListView.as_view(), name='exercise_list'),
    path('exercise/<int:exercise_id>/', views.exercise_detail, name='exercise_detail'),
    path('workout/', views.workout_list, name='workout_list'),
    path('workout/<int:workout_id>/', views.workout_detail, name='workout_detail'),
]


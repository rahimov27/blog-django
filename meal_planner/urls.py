from django.urls import path
from . import views

urlpatterns = [
    path("meal_planner/", views.meal, name="meal_planner"),
]

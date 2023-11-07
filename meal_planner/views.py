from django.shortcuts import render, HttpResponse


# Create your views here.
def meal(request):
    return HttpResponse("Meal")

from django.shortcuts import render, HttpResponse
from .import models

recipes = [
    {
     'author': 'Simon',
     'title': 'Spaghetti Bolognese',
     'directions': 'Lorem ipsum dolor sit amet',
     'date_posted': 'July 1st, 2024'
    },
    {
     'author': 'Emma-Louise',
     'title': 'Spanish Chicken',
     'directions': 'Lorem ipsum dolor sit amet',
     'date_posted': 'July 1st, 2024'
    },
    {
     'author': 'Sienna',
     'title': 'Super Noodles',
     'directions': 'Lorem ipsum dolor sit amet',
     'date_posted': 'July 1st, 2024'
    }
]
# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, "recipes/home.html", context)
    
def about(request):
    return render(request, "recipes/about.html", {'title': 'about us page'})
    
  
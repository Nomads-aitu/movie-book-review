from django.shortcuts import render
from .models import MediaItem

def home(request):
    return render(request, 'reviews/home.html')

def movie_list(request):
    # This grabs movies AND their linked reviews efficiently
    movies = MediaItem.objects.filter(category='Movie').prefetch_related('reviews')
    return render(request, 'reviews/list.html', {'items': movies, 'title': 'Movies'})

def book_list(request):
    # This grabs books AND their linked reviews efficiently
    books = MediaItem.objects.filter(category='Book').prefetch_related('reviews')
    return render(request, 'reviews/list.html', {'items': books, 'title': 'Books'})

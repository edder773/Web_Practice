from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def index(request):
    movies = Movie.objects.all()
    content = {'movies':movies}
    return render(request,'movies/index.html', content)

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail',movie.pk)
    else:
        form = MovieForm()
    content = {'form' : form}
    return render(request, 'movies/create.html', content)

def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    content = {'movie': movie}
    return render(request, 'movies/detail.html', content)


def delete(reqeust, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')

def update(request, pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
        return redirect('movies:detail', pk=movie.pk)
    else :
        form = MovieForm(instance=movie)
    content = {'form':form, 'movie':movie}
    return render(request, 'movies/update.html',content) 
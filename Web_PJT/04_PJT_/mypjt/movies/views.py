from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie
from django.views.decorators.http import require_http_methods
import requests
# Create your views here.


def popular_count():
    url = 'https://api.themoviedb.org/3'#TMDB URL
    path = '/movie/popular' # 인기 목록
    params = {
        'api_key' : 'aa78b1e41cee22b6cb5d538019b4897d', #api key 설정
        'language' : 'ko', #언어 설정
        'region' : 'KR' #지역 설정
    }
    response = requests.get(url + path, params=params).json()
        
    return response['results'] #result 결과 반환


@require_http_methods(['GET'])
def index(request):
    # movies = Movie.objects.all()
    movies = popular_count()
    content = {'movies': movies,
               'path': 'https://image.tmdb.org/t/p/w500'}
    return render(request, 'movies/index.html', content)

@require_http_methods(['GET','POST'])
def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail',movie.pk)
    else:
        form = MovieForm()
    content = {'form': form}
    return render(request, 'movies/create.html', content)

@require_http_methods(['GET'])
def detail(request,pk):
    movie = Movie.objects.get(pk=pk)
    content = {'movie':movie}
    return render(request,'movies/detail.html',content)

@require_http_methods(['GET','POST'])
def update(request,pk):
    movie = Movie.objects.get(pk=pk)
    if request.method == 'POST':
            form = MovieForm(request.POST, request.FILES, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail',pk=movie.pk)
    else :
        form = MovieForm(instance=movie)
    content = {'form':form, 'movie':movie}
    return render(request, 'movies/update.html',content)

@require_http_methods(['POST'])
def delete(request,pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()
    return redirect('movies:index')
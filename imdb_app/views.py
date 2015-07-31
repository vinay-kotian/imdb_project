from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from models import MovieDetails
from imdb_app.serializers import MovieSerialzers



class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)



@api_view(['GET', 'POST'])
def movie_list(request):
    """
    List all 'MovieDetails', or create a new 'MovieDetail'.
    """
    if request.method == 'GET':
        movie_details = MovieDetails.objects.all()
        serializer = MovieSerialzers(movie_details, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerialzers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, name):
    """
    Retrieve, update or delete a 'MovieDetails' instance.
    """
    try:
        movie_details = MovieDetails.objects.filter(name__contains=name)
    except MovieDetails.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MovieSerialzers(movie_details,  many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieSerialzers(movie_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def directors_list(request, director_name):
    """ This views returns the list of details for the director.
    """
    if request.method == 'GET':
        movie_details = MovieDetails.objects.filter(director__contains=director_name)
        serializer = MovieSerialzers(movie_details, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def genre_list(request, genre):
    """ This views returns the list of details for the genre.
    """
    if request.method == 'GET':
        movie_details = MovieDetails.objects.filter(genre__genre_type__contains=genre)
        serializer = MovieSerialzers(movie_details, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def recomended_movies(request, movie_name):
    """ If a user searcher for movie, this api will try and find which movies are related to it. Its like finding the
    taste of the user. The search will be based on genre, director.
    """
    if request.method == 'GET':
        movie_obj = MovieDetails.objects.filter(name__contains=movie_name)
        directors_lists, genre_lists = [], []
        for movie in movie_obj:
            for genre in  movie.genre.all():
                genre_lists.append(genre)
            # f = lambda x: [genre for in movie.genre.all()]]
            directors_lists.append(movie.director)
        directors_lists, genre_lists = list(set(directors_lists)), list(set(genre_lists))
        recomended_movies_qs = MovieDetails.objects.filter(Q(director__in=directors_lists) | Q(genre__genre_type__in=genre_lists ))
        serializer = MovieSerialzers(recomended_movies_qs, many=True)
        return Response(serializer.data)

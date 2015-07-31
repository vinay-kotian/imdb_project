__author__ = 'vinay'

import json
from imdb_app.models import GenreCategory
from imdb_app.models import MovieDetails
import django
django.setup()

json_data = json.load(open('imdb.json'))

for each_data in json_data:
    for genure in each_data[u'genre']:
        GenreCategory.objects.get_or_create(genre_type=genure.strip())
    md = MovieDetails(name=each_data[u'name'], imdb_score=each_data[u'imdb_score'], popularity=each_data[u'popularity'],
                      director=each_data[u'director'])
    aa = md.save()
    for a in each_data[u'genre']:
        md.genre.add(GenreCategory.objects.get(genre_type=str(a).strip()))
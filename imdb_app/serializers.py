from rest_framework import serializers
from rest_framework import filters
from models import UserProfile
from models import MovieDetails
from models import GenreCategory


class GenreCategorySerialze(serializers.ModelSerializer):
    """ This is Genre Category Serializer. It Serializes the Genre Category Model which hold all the Genre's.
    """
    class Meta:
        model = GenreCategory
        fields = ('genre_type',)
        # read_only_fields = ('id',)


class MovieSerialzers(serializers.ModelSerializer):
    """ This is Movie Serializer class. It Serializes the Movie Details Model.
    """
    genre = serializers.SlugRelatedField(many=True, read_only='False', slug_field='genre_type')
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('name', 'imdb_score', 'popularity')

    class Meta:
        model = MovieDetails
        fields = ('name', 'imdb_score', 'popularity', 'director', 'genre',)

    def create(self, validated_data):
        """
        Create and return a new `MovieDetail` instance, given the validated data.
        """
        return MovieDetails.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `MovieDetail` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.imdb_score = validated_data.get('imdb_score', instance.imdb_score)
        instance.popularity = validated_data.get('popularity', instance.popularity)
        instance.director = validated_data.get('director', instance.director)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.save()
        return instance



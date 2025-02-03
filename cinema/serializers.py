from rest_framework import serializers
from .models import CinemaHall, Genre, Actor, Movie, MovieSession


class MovieSerializer(serializers.ModelSerializer):
    genres = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name",
    )
    actors = serializers.SlugRelatedField(
        many=True, read_only=True, slug_field="first_name"
    )

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class MovieDetailSerializer(MovieSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "description", "duration", "genres", "actors")


class MovieSessionSerializer(serializers.ModelSerializer):
    movie_title = serializers.CharField(
        source="movie.title",
        read_only=True,
    )

    cinema_hall_name = serializers.CharField(
        source="cinema_hall.name",
        read_only=True,
    )

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie_title", "cinema_hall_name")


class CinemaHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaHall
        fields = ("id", "name", "rows", "seats_in_row", "capacity")


class MovieSessionDetailSerializer(MovieSessionSerializer):
    movie = MovieSerializer(read_only=True)

    cinema_hall = CinemaHallSerializer(read_only=True)

    class Meta:
        model = MovieSession
        fields = ("id", "show_time", "movie", "cinema_hall")

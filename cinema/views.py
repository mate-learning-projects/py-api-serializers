from rest_framework import viewsets
from .models import Movie, MovieSession, CinemaHall, Genre, Actor
from .serializers import (
    MovieDetailSerializer,
    MovieSerializer,
    MovieSessionSerializer,
    MovieSessionDetailSerializer,
    CinemaHallSerializer,
    GenreSerializer,
    ActorSerializer,
)


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":

            return MovieDetailSerializer
        return MovieSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ["list", "retrieve"]:
            queryset = queryset.prefetch_related("genres", "actors")
        return queryset


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return MovieSessionDetailSerializer
        return MovieSessionSerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action in ["list", "retrieve"]:
            queryset = queryset.select_related("movie", "cinema_hall")
        return queryset

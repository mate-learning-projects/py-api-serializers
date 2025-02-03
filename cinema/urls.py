from django.urls import include, path
from rest_framework import routers
from .views import (
    ActorViewSet,
    CinemaHallViewSet,
    GenreViewSet,
    MovieSessionViewSet,
    MovieViewSet,
)

router = routers.DefaultRouter()
router.register(r"movies", MovieViewSet)
router.register(r"movie-sessions", MovieSessionViewSet)
router.register(r"cinema-halls", CinemaHallViewSet)
router.register(r"genres", GenreViewSet)
router.register(r"actors", ActorViewSet)


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "cinema"

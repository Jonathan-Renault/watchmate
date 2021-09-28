from django.urls import path
#from watchmate_app.api.views import movie_list, movie_detail
from watchmate_app.api.views import MovieListAV, MovieDetailAV


# urlpatterns = [
#     path('list/', movie_list, name='movie-list'),
#     path('<int:pk>/', movie_detail, name='movie-detail'),
# ]

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie-detail'),
]

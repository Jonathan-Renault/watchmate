from django.urls import path
from watchmate_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetailAV

# urlpatterns = [
#     path('list/', movie_list, name='movie-list'),
#     path('<int:pk>/', movie_detail, name='movie-detail'),
# ]

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),

    path('stream/', StreamPlatformAV.as_view(), name='platform-list'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='platform-detail'),

]

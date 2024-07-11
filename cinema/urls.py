from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('room/<int:room_id>/', views.movie_list, name='movie_list'),
    path('showtime/<int:showtime_id>/', views.seat_list, name='seat_list'),
]
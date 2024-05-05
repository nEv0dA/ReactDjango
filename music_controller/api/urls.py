from django.urls import path
from .views import RoomView

# Note: if use "path('home', RoomView.as_view())" it does not work.
urlpatterns = [
    path('room', RoomView.as_view()),
]
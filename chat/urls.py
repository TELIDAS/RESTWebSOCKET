from django.urls import path
from chat import views

urlpatterns = [
    path('room/', views.Rooms.as_view()),
    path('dialog/', views.Dialog.as_view()),
    path('users/', views.Rooms.as_view()),

]
from django.urls import path

from api import views

urlpatterns = [
    path('user/',views.UserView.as_view()),
    path('computer/',views.ComputerAPIView.as_view()),
]
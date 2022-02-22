
from django.urls import path
from profiles_api import views


urlpatterns = [
    path('hola-view/',views.HelloApiView.as_view()),
]

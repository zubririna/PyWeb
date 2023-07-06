from django.urls import path

from .views import CurrentDateView, HelloWorld, RandomNumber, IndexView

urlpatterns = [
    path ('', IndexView.as_view()),
    path('datetime/', CurrentDateView.as_view()),
    path('hello_world/', HelloWorld.as_view()),
    path('random_number/', RandomNumber.as_view()),
]
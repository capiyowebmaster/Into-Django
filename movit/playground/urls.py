
from django.urls import path
from .  import   views


#url config fro every app
urlpatterns=[
    path('hello/', views.say_hello)
]
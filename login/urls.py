from django.urls import path
from .views import *
urlpatterns = [
    path('', login_, name="login"),
    path('/signup', signup, name="signup"),
    path('/logout', logout_, name="logout_"),
]

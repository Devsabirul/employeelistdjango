from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="HOME"),
    path("add-employee", add_employee, name="add_employee"),
    path("update-employee/<int:pk>", update_employee, name="update_employee"),
    path("delete/<int:pk>", delete, name="delete"),
]

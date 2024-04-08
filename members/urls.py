# Importing necessary modules
from django.urls import path
from . import views

# Define URL patterns
urlpatterns = [
    # URL pattern for the main page, calls the 'main' function in views.py
    path('', views.main, name='main'),

    # URL pattern for the members page, calls the 'members' function in views.py
    path('members/', views.members, name='members'),

    # URL pattern for displaying details of a member with a specific ID,
    # calls the 'details' function in views.py
    # The <slug:slug> part indicates that an slug parameter with name 'slug' will be passed
    path('members/details/<slug:slug>', views.details, name='details'),

    # URL pattern for the testing page, calls the 'testing' function in views.py
    path('testing/', views.testing, name='testing'),
]

from django.urls import path
from .views import *
urlpatterns = [
    path('profile/<int:userid>',profile),
    path('view_profile/',view_profile),
    path('post/',post_view)
]

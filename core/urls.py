from django.urls import path
from .views import *
urlpatterns = [
    path('profile/<int:userid>',profile),
    path('view_profile/<str:username>',view_profile),
    path('post/',post_view),
    path('viewpost/', PostofUser),
    path('viewpost/<int:id>/',viewPostDetail,name='view_post_detail'),

    
]

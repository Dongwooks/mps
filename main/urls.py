from django.urls import path
from . import views


urlpatterns = [
    
    path('section1/', views.section1),
    path('tag_section1/', views.tag_section1),    
    path('director_list/', views.director_list),
    path('actor_list/', views.actor1_list),

    path('section2/', views.section2),
    path('tag_section2/', views.tag_section2),
    path('movie_list/', views.movie_list),
    path('actor_list2/', views.actor2_list),
    
    path('result/', views.result),
    
    path('home', views.home),   
]

from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.starting_page,name="home"),
    path("posts/" ,views.all_post,name="all-post"),
    path("posts/<slug:slug>",views.single_post_page, name="single_post")
    
]

from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.StartPageView.as_view(),name="home"),
    path("posts/" ,views.AllPostView.as_view(),name="all-post"),
    path("posts/<slug:slug>",views.SinglePostView.as_view(), name="single_post")
    
]

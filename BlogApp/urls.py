from django.urls import path
from . import views

urlpatterns = [
    path('Blog', views.Blog, name="Blog"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('about',views.about, name="about"),
    path('signup',views.signup, name="signup"),
    path('log_in',views.log_in, name="log_in"),
    path('log_out',views.log_out, name="logout"),
    path('addpost',views.add_post, name="addpost"),
    path('updatepost/<int:id>/',views.update_post, name="updatepost"),
    path('<int:id>',views.delete_post, name="deletepost"),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("Project/<int:pk>/", views.project_detail, name="project_detail"),
    path("service/<int:pk>/",views.service_detail, name="service_detail"),
]
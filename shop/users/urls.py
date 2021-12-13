from django.urls import path

from . import views

urlpatterns = [
    path("customers/", views.CustomerListView.as_view()),
    path("customers/<int:pk>", views.CustomerDetailView.as_view()),
]

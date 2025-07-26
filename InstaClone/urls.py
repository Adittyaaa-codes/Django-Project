from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('post',views.create_post),
    # path('delete',views.delete_post),
]
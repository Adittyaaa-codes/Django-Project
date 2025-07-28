from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_page'),
    path('post',views.create_post,name='create_post'),
    path('delete/<int:post_id>/',views.delete_post,name='confirm_delete'),
    path('like/', views.toggle_like, name='toggle_like'),
    path('comments/<int:post_id>/', views.view_comments, name='view_comments'),
    path('comment/<int:post_id>/', views.post_comment, name='post_comment'),
]
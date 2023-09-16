from django.urls import path,include
from news.api import views


urlpatterns = [
    path('news/',views.NewsListorCreateApiView.as_view({'get': 'list', 'post': 'create'}),name='news'),
    path('news/<int:pk>',views.NewsListorCreateApiView.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),name='news-detail'),
    path('journalists/',views.JournalistListorCreateApiView.as_view(),name='journalists'),
    path('journalists/<int:pk>/',views.JournalistDetailApiView.as_view(),name='journalist-detail'),
    path('profiles/',views.ProfileListOrCreateApiView.as_view(),name='profiles'),
    path('profiles/<int:pk>/',views.ProfiletDetailApiView.as_view(),name='profile-detail'),
    path('news/<int:article_id>/comment/',views.CommentAddApiView.as_view(),name='comment'),
    path('comments/',views.CommentListApiView.as_view(),name='comments'),
    path('profiles/add_pphoto/', views.ProfilePhotoApiView.as_view(), name='profile-photo'),
    path('register/',views.RegisterApi.as_view(),name='register')

]

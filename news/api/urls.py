from django.urls import path,include
from news.api import views
urlpatterns = [
    path('news/',views.NewsListorCreateApiView.as_view(),name='news'),
    path('news/<int:pk>',views.NewsDetailApiView.as_view(),name='news-detail'),
    path('journalists/',views.JournalistListorCreateApiView.as_view(),name='journalists'),
    path('journalists/<int:pk>/',views.JournalistDetailApiView.as_view(),name='journalist-detail'),
    path('profiles/',views.ProfileListOrCreateApiView.as_view(),name='profiles'),
    path('profiles/<int:pk>/',views.ProfiletDetailApiView.as_view(),name='profile-detail'),
    path('news/<int:article_id>/comment/',views.CommentAddApiView.as_view(),name='comment'),
    path('comments/',views.CommentListApiView.as_view(),name='comments'),



]

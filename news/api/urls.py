from django.urls import path,include
from news.api import views
urlpatterns = [
    path('news/',views.NewsListorCreateApiView.as_view(),name='news'),
    path('news/<int:pk>',views.NewsDetailApiView.as_view(),name='news-detail'),
    path('journalists/',views.JournalistListorCreateApiView.as_view(),name='journalists'),
    path('journalists/<int:pk>',views.JournalistDetailApiView.as_view(),name='journalist-detail'),



]

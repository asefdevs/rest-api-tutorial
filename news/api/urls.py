from django.urls import path,include
from news.api import views
urlpatterns = [
    path('news/',views.NewsListorCreateApiView.as_view(),name='news'),
    path('journalists/',views.JournalistListorCreateApiView.as_view(),name='journalists'),
]

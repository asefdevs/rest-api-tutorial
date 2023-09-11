from rest_framework import status
from rest_framework.response import Response 

from news.models import Article, Journalist
from news.api.serializers import NewsSerializer, JournalistSerializer

#class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class NewsListorCreateApiView(APIView):

    def get(self,request):
        news=Article.objects.all()
        serializer=NewsSerializer(news,many=True)
        return Response(serializer.data)
    
    
    def post(self,request):
        serializer=NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


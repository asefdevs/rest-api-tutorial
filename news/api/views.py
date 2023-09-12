from rest_framework import status
from rest_framework.response import Response 

from news.models import Article, Journalist,Profile
from news.api.serializers import NewsSerializer, JournalistSerializer,ProfileSerializer

#class views
# from rest_framework.views import APIView
# from rest_framework.generics import get_object_or_404
from rest_framework import generics
from news.api.permissions import IsAuthenticatedOrAdminOrPorifleowner

class NewsListorCreateApiView(generics.ListCreateAPIView):
    queryset=Article.objects.all()
    serializer_class=NewsSerializer
    permission_classes=[IsAuthenticatedOrAdminOrPorifleowner]


class JournalistListorCreateApiView(generics.ListCreateAPIView):
    queryset=Journalist.objects.all()
    serializer_class=JournalistSerializer

class NewsDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=NewsSerializer

class JournalistDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Journalist.objects.all()
    serializer_class=JournalistSerializer

class ProfileListOrCreateApiView(generics.ListCreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer

class ProfiletDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer






# class NewsListorCreateApiView(APIView):

#     def get(self,request):
#         news=Article.objects.all()
#         serializer=NewsSerializer(news,many=True)
#         return Response(serializer.data)
    

#     def post(self,request):
#         serializer=NewsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class JournalistListorCreateApiView(APIView):

#     def get(self,request):
#         journalists=Journalist.objects.all()
#         serializer=JournalistSerializer(journalists,many=True,context={'request': request})
#         return Response(serializer.data)
#     def post(self,request):
#         serializer=JournalistSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# class NewsDetailApiView(APIView):
#     def get_object(self,pk):
#         instance=get_object_or_404(Article,pk=pk)
#         return instance

#     def get(self,request,pk):
#         article=self.get_object(pk=pk)
#         serializer=NewsSerializer(article)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         article=self.get_object(pk=pk)
#         serializer=NewsSerializer(article,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         article=self.get_object(pk=pk)
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class JournalistDetailApiView(APIView):
#     def get_object(self,pk):
#         instance=get_object_or_404(Journalist,pk=pk)
#         return instance

#     def get(self,request,pk):
#         journalist=self.get_object(pk=pk)
#         serializer=JournalistSerializer(journalist,context={'request': request})
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         journalist=self.get_object(pk=pk)
#         serializer=JournalistSerializer(journalist,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         journalist=self.get_object(pk=pk)
#         journalist.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import status
from rest_framework.response import Response 
from rest_framework import permissions
from news.models import Article, Journalist,Profile,Comment
from news.api.serializers import NewsSerializer, JournalistSerializer,ProfileSerializer,UserSerializer,CommentSerializer,ProfilePhotoSerializer
#class views
# from rest_framework.views import APIView
# from rest_framework.generics import get_object_or_404
from rest_framework import generics
from news.api.permissions import IsAuthenticatedOrAdmin
from news.api.pagination import CustomPagination
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
from dj_rest_auth.views import LoginView as restlogin,LogoutView as restlogout
from django.contrib.auth.models import User

class RegisterApi(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

# class LoginApi(restlogin):
#     pass

# class LogoutApi(restlogout):
#     pass


# class NewsListorCreateApiView(generics.ListCreateAPIView):
#     queryset=Article.objects.all()
#     serializer_class=NewsSerializer
#     permission_classes=[IsAuthenticatedOrAdmin]
#     pagination_class=CustomPagination
#     filter_backends=[SearchFilter]
#     search_fields=['title']
class NewsListorCreateApiView(viewsets.ModelViewSet):
    queryset=Article.objects.all()
    serializer_class=NewsSerializer
    permission_classes=[IsAuthenticatedOrAdmin]
    pagination_class=CustomPagination
    filter_backends=[SearchFilter]
    search_fields=['title']




class JournalistListorCreateApiView(generics.ListCreateAPIView):
    queryset=Journalist.objects.all()
    serializer_class=JournalistSerializer
    permission_classes=[IsAuthenticatedOrAdmin]


# class NewsDetailApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset=Article.objects.all()
#     serializer_class=NewsSerializer
#     permission_classes=[IsAuthenticatedOrAdmin]



class JournalistDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Journalist.objects.all()
    serializer_class=JournalistSerializer
    permission_classes=[IsAuthenticatedOrAdmin]


class ProfileListOrCreateApiView(generics.ListCreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[permissions.IsAdminUser]

class ProfiletDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer

class CommentAddApiView(generics.CreateAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[permissions.IsAuthenticated]


    def perform_create(self, serializer):
        article_id = self.kwargs.get('article_id')
        try :
            article=Article.objects.get(pk=article_id)
        except Article.DoesNotExist:
            raise Exception('Article doesnt exist')
        
        if article:
            serializer.save(user=self.request.user, article=article)
        else:
            pass


class CommentListApiView(generics.ListAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=[IsAuthenticatedOrAdmin]



class ProfilePhotoApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfilePhotoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        instance = self.request.user.profile  
        return instance    
    

    # queryset=Profile.objects.all()
    # lookup_field = 'user__pk' 


    # def perform_create(self, serializer):
    #     user=self.request.user
    #     serializer.save(user=user)

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

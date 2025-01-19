from django.shortcuts import render
from .serializers import UserRegistrationSerializer,BlogSerialzier,UpdateUserProfileSerializer,UserInfoSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Blog
from rest_framework.pagination import PageNumberPagination
# Create your views here.

class BlogListPagination(PageNumberPagination):
    page_size = 1

@api_view(["GET"])
def blog_list(request):
    blogs = Blog.objects.all()
    paginator = BlogListPagination()
    paginated_blog = paginator.paginate_queryset(blogs,request)
    serializer = BlogSerialzier(paginated_blog,many=True)
    return paginator.get_paginated_response(serializer.data)

# @api_view(['GET'])
# def blog_list(request):
#     blogs = Blog.objects.all()
#     serializer = BlogSerializer(blogs, many=True)
#     return Response(serializer.data)
@api_view(['GET'])
def get_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    serializer = BlogSerialzier(blog)
    return Response(serializer.data)

@api_view(["POST"])
def register_user(request):
    serializer = UserRegistrationSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_profile(request):
    user = request.user
    serializer = UpdateUserProfileSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_blog(request):
    user = request.user
    serializer = BlogSerialzier(data = request.data)
    if serializer.is_valid():
        serializer.save(author = user)
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(["POST"])
# def create_blog(request):
#     serializer = BlogSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def blog_update(request,pk):
    user = request.user
    blog = Blog.objects.get(id=pk)
    if blog.author !=user:
        return Response({"error":"You are not author of this blog"},status=status.HTTP_403_FORBIDDEN)
    serializer = BlogSerialzier(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

# @api_view(["PUT"])
# def blog_update(request, pk):
#     blog = Blog.objects.get(id=pk)
#     serializer = BlogSerializer(blog, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def blog_delete(request,pk):
    user = request.user
    blog = Blog.objects.get(id=pk)
    if blog.author !=user:
        return Response({"error":"You are not author of this blog"},status=status.HTTP_403_FORBIDDEN)
    blog.delete()
    return Response({"message":"Blog Deleted Successfully"},status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_username(request):
    user = request.user
    username = user.username
    return Response({"username":username})

@api_view(['GET'])
def get_userinfo(request, username):
    User = get_user_model()
    user = User.objects.get(username=username)
    serializer = UserInfoSerializer(user)
    return Response(serializer.data)
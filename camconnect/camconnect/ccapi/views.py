from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from .serializer import PostSerializer
from .models import Post

class PostView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

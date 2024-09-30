from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        # Delete all blog posts
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def get_queryset(self):
        title = self.request.query_params.get('title', None)
        if title:
            return BlogPost.objects.filter(title__icontains=title)
        return BlogPost.objects.all()

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
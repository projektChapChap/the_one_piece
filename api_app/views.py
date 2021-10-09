from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from .models import Post
from django.shortcuts import get_object_or_404


class PostViews(APIView):
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
   
    def get(self, request, tarehe=None):
        if tarehe:
            item = Post.objects.get(tarehe=tarehe)
            serializer = PostSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = Post.objects.all()
        serializer = PostSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
    
    
    def patch(self, request, id=None):
        item = Post.objects.get(id=id)
        serializer = PostSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})


   
    def delete(self, request, id=None):
        item = get_object_or_404(Post, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
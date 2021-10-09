from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    tarehe = serializers.CharField(max_length=200)
    jina = serializers.CharField(max_length=200)
    maelezo = serializers.CharField(max_length=200)
    mmuda = serializers.DateField()
    picha = serializers.ImageField()

    class Meta:
        model = Post
        fields = ('__all__')
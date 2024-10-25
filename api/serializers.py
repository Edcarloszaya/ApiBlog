from rest_framework import serializers
from .models import Post

# serializers para  serializar e desserializar dados do banco
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'content','tags', 'createdAt', 'updatedAt']
# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PostSerializer
from .models import Post


# View para criar , lista e filtra os posts
@api_view(["GET", "POST"])
def list_or_create_post(request):

    #  lista e filtra o post
    if request.method == "GET":
        term = request.query_params.get("term", None)
        if term:
            posts = Post.objects.filter(tags__icontains=term)
            if not posts:
                return Response(
                    {"message": "Nenhum post encontrado para a tag.", "posts": []},
                    status=status.HTTP_200_OK,
                )
        else:
            posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # cria o post
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # View para lista , atualiza e deleta um unico post por id
@api_view(["GET", "PUT", "PATCH", "DELETE"])
def retrieve_update_destroy_post(request, id):

    # obtem o post do banco de dados se tiver
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return Response(
            {"error": "Postagem não encontrada."}, status=status.HTTP_404_NOT_FOUND
        )

    # lista o post por
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # atualçiza o post
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # atualiza um unico campo do post
    elif request.method == "PATCH":
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # deleta o post
    elif request.method == "DELETE":
        post.delete()
        return Response(
            {"message": "Postagem deletada com sucesso."},
            status=status.HTTP_204_NO_CONTENT,
        )

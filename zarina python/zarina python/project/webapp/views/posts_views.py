from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from webapp.models import Post, PostImage
from webapp.serializers import PostCreateUpdateSerializer, PostImageSerializer, PostDetailSerializer
from rest_framework.exceptions import PermissionDenied


class PostListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostDetailSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetailView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = PostDetailSerializer(post)
        return Response(serializer.data)


class PostCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Сериализуем данные из запроса
        serializer = PostCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            post = serializer.save(user=request.user)  # user назначается через токен
            images = request.FILES.getlist('images')  # Получаем список изображений
            for image in images:
                PostImage.objects.create(post=post, image=image)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        if post.user != request.user:
            raise PermissionDenied("You do not have permission to edit this post.")

        serializer = PostCreateUpdateSerializer(post, data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            if 'images' in request.FILES:
                new_images = request.FILES.getlist('images')
                PostImage.objects.filter(post=post).delete()
                for image in new_images:
                    PostImage.objects.create(post=post, image=image)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)

        if post.user != request.user:
            raise PermissionDenied("You do not have permission to delete this post.")

        post.delete()
        return Response({"detail": "Post deleted successfully."}, status=status.HTTP_204_NO_CONTENT)

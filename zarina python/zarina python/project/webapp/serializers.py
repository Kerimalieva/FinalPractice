from .models import CustomUser
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken
from .models import Post, PostImage
from django.contrib.auth import get_user_model
from rest_framework import serializers


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']


class PostDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Включаем информацию о пользователе (авторе)
    images = PostImageSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'status', 'user', 'images', 'created_at', 'updated_at']


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'status', 'images', 'created_at', 'updated_at']

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance


class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("The two password fields must match.")
        return data

    def validate_token(self, access_token):
        try:
            token = AccessToken(access_token)
            user = CustomUser.objects.get(id=token['user_id'])
        except Exception as e:
            raise AuthenticationFailed("Invalid or expired token.")
        return user

    def save(self, validated_data, access_token):
        user = self.validate_token(access_token)
        user.set_password(validated_data['new_password'])
        user.save()
        return user

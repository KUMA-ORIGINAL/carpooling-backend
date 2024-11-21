from rest_framework import serializers

from rides.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'rating', 'photo', 'is_verified']

#
# class UserCreateSerializer(UserCreateSerializer):
#     class Meta(UserCreateSerializer.Meta):
#         model = User
#         fields = ('id', 'email', 'username', 'first_name', 'last_name',
#                   'password')
#
#
# class UserSerializer(UserSerializer):
#     articles = ArticleListSerializer(many=True, read_only=True)
#
#     class Meta(UserSerializer.Meta):
#         fields = ('id', 'email', 'username', 'first_name', 'last_name',
#                   'photo', 'role', 'official', 'articles')
from djoser.serializers import UserCreateSerializer, UserSerializer

from .models import User


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'full_name', 'password')


class UserSerializer(UserSerializer):

    class Meta(UserSerializer.Meta):
        fields = ('id', 'email', 'full_name', 'role')
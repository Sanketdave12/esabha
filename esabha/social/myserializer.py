from rest_framework import serializers
from social.models import PostLike, MyPost, PostComment, FollowUser, MyProfile
from django.contrib.auth.models import User


class PostLikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostLike
        fields = "__all__"

class MyPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyPost
        fields = "__all__"

class PostCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostComment
        fields = "__all__"

class FollowUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FollowUser
        fields = "__all__"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class MyProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyProfile
        fields = "__all__"
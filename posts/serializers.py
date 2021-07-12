from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from posts.models import PostModel


class PostsSerializer(ModelSerializer):

    subject = serializers.CharField(min_length=15, max_length=250)
    author = serializers.CharField(min_length=5, max_length=100)
    content = serializers.CharField(validators=[
        RegexValidator('^[.*]{50,2000}$', 'Min 50, max 2000')
    ])

    class Meta:
        model = PostModel
        fields = '__all__'

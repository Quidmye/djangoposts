from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import PostModel
from posts.serializers import PostsSerializer


class PostsViewCreate(APIView):

    def get(self, *args, **kwargs):
        qs = PostModel.objects.all()
        serializer = PostsSerializer(qs, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):

        data = self.request.data

        serializer = PostsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class PostsViewDeleteUpdate(APIView):

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')

        post = get_object_or_404(PostModel, pk=pk)

        serializer = PostsSerializer(post)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')

        data = get_object_or_404(PostModel, pk=pk)

        data.delete()
        return Response('delete', status.HTTP_204_NO_CONTENT)

    def patch(self, *args, **kwargs):

        pk = kwargs.get('pk')
        body = self.request.data

        data = get_object_or_404(PostModel, pk=pk)

        serializer = PostsSerializer(data, data=body, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_202_ACCEPTED)

    def put(self, *args, **kwargs):

        pk = kwargs.get('pk')
        body = self.request.data

        data = get_object_or_404(PostModel, pk=pk)
        serializer = PostsSerializer(data, data=body)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_202_ACCEPTED)

from rest_framework import serializers
from ..models import Post

# this is very first model serializer. So i can use postman to query  that particular board post, and
#it will give me a serialized data, from it.
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['author','title','content','date_posted']


class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['author','id','title','content','date_posted']


# So now in my first view here, I list out all my posts that I have.

from rest_framework.generics import ListAPIView,RetrieveAPIView, UpdateAPIView,DestroyAPIView,CreateAPIView
from ..models import Post
from .serializers import PostSerializer,PostCreateSerializer

class PostListAPIView(ListAPIView):
    queryset =  Post.objects.all()
    serializer_class = PostSerializer

    #I can try to customize these views using certain methods, like how i want these views to work.

#Here I will use RetrieveAPIView for getting post details. Let's implement it.
#After ceratign a class here for such a retrieval, let's create a url also for this api.

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


#Let's say if I want a different look for my post detail, then I can make a different Post Detail serializer.
#I make this new look Post Detail Serializer in my serializers.py file.


'''Now we are gonna create an update and destroy/delete api view.'''

class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer

    #Here we write a function that basically requests the user who is creating the post.

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)



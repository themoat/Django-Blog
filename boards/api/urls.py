"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path

from .. import views
from ..views import PostListView
from.views import PostListAPIView,PostDetailAPIView,PostUpdateAPIView,PostDeleteAPIView,PostCreateAPIView

urlpatterns = [
    #path('admin/', admin.site.urls),

    # path('about',views.about, name='boards-about'),
    path("/", PostListAPIView.as_view(), name='posts-api'),
    path('/int:<pk>',PostDetailAPIView.as_view(),name = 'post-details'),
    path('/int:<pk>/update',PostUpdateAPIView.as_view(),name = 'post-updates'),
    path('/int:<pk>/delete',PostDeleteAPIView.as_view(),name = 'post-deletes'),
    path('/create',PostCreateAPIView.as_view(),name = 'post-creates'),
    # path('post/<int:pk>/',PostDetailView.as_view(), name = 'post-detail'),
    # path('post/new',PostCreateView.as_view(), name = 'post-create'),
    # path('post/<int:pk>/update',PostUpdateView.as_view(), name = 'post-update')

]




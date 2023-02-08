from django.urls import path, include
from applications.post.views import *

urlpatterns = [
#     path('', PostListAPIVIEW.as_view()),
#     path('create/', PostCreateAPIVIEW.as_view()),
#     path('update/<int:pk>', PostCreateAPIVIEW.as_view()),
#     path('delete/<int:pk>', PostUpdateAPIVIEW.as_view()),
#     path('detail/<int:id>', PostDetailAPIVIEW.as_view()),

    path('', PostListCreateAPIView.as_view()),
    path('<int:pk>/', PostDetailDeleteUpdateAPIView.as_view())
]
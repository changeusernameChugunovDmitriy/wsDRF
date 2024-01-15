from django.urls import path
from rest_framework import routers

from .views import *

# router = routers.DefaultRouter()
# router.register(r'posts', PostsView)
#
# urlpatterns = router.urls

urlpatterns = [
    path('posts/', bookList),
    path('posts/<int:pk>/', bookGet),
    path('posts/del/<int:pk>/', bookDelete),
    path('posts/create/', bookCreate),
    path('posts/update/<int:pk>', bookPut),
]
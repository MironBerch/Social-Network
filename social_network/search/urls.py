from django.urls import path

from posts.views import (

)


urlpatterns = [
    path(
        route='', 
        view=PostAPIView.as_view(), 
        name='post'),
]
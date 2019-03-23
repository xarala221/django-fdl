from django.urls import path
from blog.views import index, about
urlpatterns = [
    path('', index ),
    path('about/', about ),

]

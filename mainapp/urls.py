from django.urls import path
from .views import *
urlpatterns = [
     path('', index, name='index'),
     path('about',about , name='about'),
     path('course',course , name='course'),
     path('teacher', teacher, name='teacher'),
     path('blog', blog, name='blog'),
     path('blog_detail', blog_detail, name='blog_detail'),
     path('contact',contact , name='contact'),
]
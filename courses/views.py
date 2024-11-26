from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializer
from .models import Courses

# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    '''A simple crud for courses'''
    serializer_class = CourseSerializer
    queryset = Courses.objects.all()
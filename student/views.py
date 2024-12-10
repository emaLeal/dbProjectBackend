from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    '''A simple crud for courses'''
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
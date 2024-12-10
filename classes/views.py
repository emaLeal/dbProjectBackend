from rest_framework import viewsets
from .serializers import ClassSerializer, MaterialSerializer, AttendanceSerializer
from .models import Classes, Material, Attendance

# Create your views here.
class ClassViewSet(viewsets.ModelViewSet):
    '''A simple crud for courses'''
    serializer_class = ClassSerializer
    queryset = Classes.objects.all()
    
class MaterialViewSet(viewsets.ModelViewSet):
    '''A simple crud for courses'''
    serializer_class = MaterialSerializer
    queryset = Material.objects.all()
    
class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    queryset = Attendance.objects.all()
    
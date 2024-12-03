from rest_framework import viewsets
from .serializers import RoleSerializer
from .models import Role

# Create your views here.
class RoleViewSet(viewsets.ModelViewSet):
    '''A simple crud for courses'''
    serializer_class = RoleSerializer
    queryset = Role.objects.all()
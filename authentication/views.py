from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
@api_view(['POST'])
def register(request):
    '''Recieves the code and password from a user and returns a token'''
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(code=serializer.data['code'])
        user.set_password(serializer.data['password'])
        user.save()
        return Response({'message': f'User {user} successfully created'}, status=201)
    return Response(serializer.errors, status=400)
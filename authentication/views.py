from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny

User = get_user_model()

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
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

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    '''Recognize the authenticated user and return it for its data to be used'''
    raw_user = request.user
    raw_user = {
        'document_id': raw_user.code,
        'name': raw_user.name,
        'state': raw_user.state,
        'email': raw_user.email,
        'username': raw_user.username
    }    
   
    return Response(raw_user, status=200)

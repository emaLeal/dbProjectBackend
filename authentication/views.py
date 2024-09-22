from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

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

@api_view(['POST'])
def login(request):
    '''Verifies the user credentials and return a token for access to the page'''
    user = get_object_or_404(User, code=request.data['code'])
    if not user.check_password(request.data['password']):
        return Response({'message': 'invalid password'}, status=400)
   
    token, created = Token.objects.get_or_create(user=user)
    print(token)
    
    return Response({"token": token.key}, status=200)
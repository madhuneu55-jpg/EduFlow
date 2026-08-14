from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer
from .serializers import UserSerializer
from django.contrib.auth.models import User
from base.models import Message
from .serializers import MessageSerializer
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET/api',
        'GET/api/rooms',
        'GET/api/rooms/:id'
    ]
    
    return Response(routes)
@api_view(['GET'])
def getRooms(request):
    rooms= Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request,pk):
    room= Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getUser(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def getMessages(request):
    messages = Message.objects.all()
    Serializer = MessageSerializer(messages, many = True)
    return Response(Serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createRoom(request):
    serializer = RoomSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def updateRoom(request,pk):
    room = room.objects.get(id=pk)
    serializer = RoomSerializer(instance=room, data = request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status = 400)


@api_view(['DELETE'])
def deleteRoom(request,pk):
    room = room.objects.get(id=pk)
    room.delete()
    
    return Response("room was deletes succcessfully")


@api_view(['POST'])
def registerUser(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)

@api_view(['POST'])
def loginUser(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(
        username=username,
        password=password
    )

    if user is not None:
        return Response({
            'message': 'Login successful',
            'username': user.username
        })

    return Response({
        'error': 'Invalid username or password'
    }, status=401)



    
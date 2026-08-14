from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .models import Room, Topic,Message
from .forms import RoomForm


# LOGIN

def loginpage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        # Empty fields
        if not username or not password:
            messages.error(
                request,
                'Please enter both username and password.'
            )
            return redirect('login')

        # Check username
        if not User.objects.filter(username=username).exists():
            messages.error(
                request,
                'Username does not exist.'
            )
            return redirect('login')

        # Authenticate user
        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        # Wrong password
        messages.error(
            request,
            'Invalid password.'
        )
        return redirect('login')

    return render(request, 'base/login_register.html')


# HOME


def home(request):

    q = request.GET.get('q', '').strip()

    rooms = Room.objects.all()
    topics = Topic.objects.all()

    if q:
        rooms = rooms.filter(
            topic__name__icontains=q
        )

    room_count = rooms.count()

    recent_messages = Message.objects.filter(
        room__name__icontains=q
    ).order_by('-created')[:10]

    context = {
        'rooms': rooms,
        'topics': topics,
        'q': q,
        'room_count': room_count,
        'recent_messages': recent_messages,
    }

    return render(request, 'base/home.html', context)







# ROOM
def room(request, pk):

    room = Room.objects.get(id=pk)
    topics = Topic.objects.all()

    room_messages = room.message_set.all()

    participants = room.participants.all()

    if request.method == 'POST':

        if not request.user.is_authenticated:
            return redirect('login')

        body = request.POST.get('body', '').strip()

        if body:
            Message.objects.create(
                user=request.user,
                room=room,
                body=body
            )

            # Add the user to room participants
            room.participants.add(request.user)

        return redirect('room', pk=room.id)

    context = {
        'room': room,
        'topics': topics,
        'room_messages': room_messages,
        'participants': participants,
    }

    return render(request, 'base/room.html', context)


#profile
def userprofile(request,pk):
    user = User.objects.get(id = pk)
    rooms = user.room_set.all()
    context = {'user':user,
               'rooms':rooms
               
               }
    return render(request,'base/profile.html',context)

# CREATE ROOM

@login_required(login_url='login')
def createRoom(request):

    form = RoomForm()

    if request.method == 'POST':

        form = RoomForm(request.POST)

        if form.is_valid():

            room = form.save(commit=False)
            room.host = request.user
            room.save()

            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'base/room_form.html', context)


# UPDATE ROOM

@login_required(login_url='login')
def updateRoom(request, pk):

    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse(
            'Only the room owner can perform this action.'
        )

    form = RoomForm(instance=room)

    if request.method == 'POST':

        form = RoomForm(
            request.POST,
            instance=room
        )

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
    }

    return render(request, 'base/room_form.html', context)


# DELETE ROOM

@login_required(login_url='login')
def deleteRoom(request, pk):

    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse(
            'Only the room owner can perform this action.'
        )

    if request.method == 'POST':
        room.delete()
        return redirect('home')

    context = {
        'room': room,
    }

    return render(request, 'base/delete.html', context)


# REGISTER

def registerpage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        # Empty fields
        if not username or not password or not password2:
            messages.error(
                request,
                'Please fill in all fields.'
            )
            return redirect('register')

        # Password confirmation
        if password != password2:
            messages.error(
                request,
                'Passwords do not match.'
            )
            return redirect('register')

        # Existing username
        if User.objects.filter(username=username).exists():
            messages.error(
                request,
                'Username already exists.'
            )
            return redirect('register')

        # Create user
        user = User.objects.create_user(
            username=username,
            password=password
        )

        # Login immediately
        login(request, user)

        return redirect('home')

    return render(request, 'base/register.html')


# LOGOUT

def logoutpage(request):

    logout(request)

    return redirect('login')


@login_required(login_url='login')
def deleteMessage(request, pk):

    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse(
            'Only the message owner can delete this message.'
        )

    if request.method == 'POST':

        room = message.room

        message.delete()

        return redirect('room', pk=room.id)

    context = {
        'message': message,
    }

    return render(
        request,
        'base/delete.html',
        context
    )
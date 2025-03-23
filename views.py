from django.shortcuts import render

def lobby(request):
    """ Renders the chat lobby where users can enter a room. """
    return render(request, 'chat/lobby.html')

def room(request, room_name):
    """ Renders the chat room dynamically based on the room name. """
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'username': request.user.username if request.user.is_authenticated else 'Guest'
    })

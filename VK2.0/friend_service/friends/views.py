# views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Friendship
from .serializers import FriendshipSerializer

@api_view(['GET'])
def get_friendship_requests(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'message': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)

    outgoing_requests = user.outgoing_friendships.all()
    incoming_requests = user.incoming_friendships.all()

    outgoing_serializer = FriendshipSerializer(outgoing_requests, many=True)
    incoming_serializer = FriendshipSerializer(incoming_requests, many=True)

    return Response({'outgoing_requests': outgoing_serializer.data, 'incoming_requests': incoming_serializer.data})

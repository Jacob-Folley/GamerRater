"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from GamerRaterAPI.models import Game
from django.core.exceptions import ValidationError


class GameView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def list(self, request):
        game = Game.objects.all()
        serializer = GameSerializer(game, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """
        
        try:
            serializer = GameSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(userId=request.auth.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id', 'title', 'description', 'designer', 'year_released', 'num_of_players', 'estimated_time', 'age', 'overall_rating']
        depth: 1
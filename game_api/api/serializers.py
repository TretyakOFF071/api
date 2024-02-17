from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Game, GameUser

class GameSerializer(ModelSerializer):

    stage_end_date = serializers.DateField(format='%d.%m.%Y')

    class Meta:
        model = Game
        fields = '__all__'

class GameUserSerializer(ModelSerializer):

    class Meta:
        model = GameUser
        fields = '__all__'








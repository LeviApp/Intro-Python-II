from rest_framework import serializers

from mic.models import City, Player, Criminal, Case, Place, Witness, Responses, Clue

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('__all__')

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('__all__')
from rest_framework import serializers
from .models import DeployedTickets


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeployedTickets
        fields = ('id', 'sponser', 'accountAddress')
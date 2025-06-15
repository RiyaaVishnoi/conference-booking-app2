from rest_framework import serializers
from .models import Room, Booking

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    room = serializers.StringRelatedField()  # shows the rooms __str__()

    class Meta:
        model = Booking
        fields = '__all__'
        read_only_fields = ['user']

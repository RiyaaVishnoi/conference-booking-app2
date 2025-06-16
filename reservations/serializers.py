from rest_framework import serializers
from .models import Room, Booking

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    room = serializers.SlugRelatedField(slug_field='name', queryset=Room.objects.all())

    class Meta:
        model = Booking
        fields = '__all__'

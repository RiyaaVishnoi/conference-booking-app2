from rest_framework import serializers
from .models import Room, Booking
from django.contrib.auth.models import User

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff', 'is_superuser']
class BookingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    room = serializers.PrimaryKeyRelatedField(queryset=Room.objects.all())
    room_name = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = ['id', 'user', 'room', 'room_name', 'date', 'time', 'purpose']

    def get_room_name(self, obj):
        return obj.room.name

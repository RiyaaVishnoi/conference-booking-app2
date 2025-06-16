from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet, BookingViewSet, CustomAuthToken, UserViewSet
from .views import RegisterUser

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/login/', CustomAuthToken.as_view()),
    path('auth/register/', RegisterUser.as_view()),
]

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


from rest_framework import generics, viewsets
from . serializers import MenuSerializer, BookingSerializer, UserSerializer
from . models import Menu, Booking
from django.contrib.auth.models import User

class MenuItemView(generics.ListCreateAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = []

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MenuSerializer
    queryset = Menu.objects.all()
    permission_classes = []
    
       
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = []
    
# class SingleBookingItemView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = BookingSerializer
#     queryset = Booking.Objects.all()
#     permission_classes = []

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [] #[permissions.IsAuthenticated] 
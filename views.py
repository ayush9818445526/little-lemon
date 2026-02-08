from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer


def index(request):
    return render(request, 'index.html')


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]

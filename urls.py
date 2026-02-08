from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet, index

router = DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
]

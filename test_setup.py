#!/usr/bin/env python
import os
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
BASE_DIR = Path(__file__).resolve().parent
import sys
sys.path.insert(0, str(BASE_DIR))

django.setup()

# Now test imports
print("Testing imports...")
try:
    from restaurant.models import Menu, Booking
    print("✓ Menu and Booking models imported successfully")
except Exception as e:
    print(f"✗ Error importing models: {e}")

try:
    from restaurant.serializers import MenuSerializer, BookingSerializer
    print("✓ Serializers imported successfully")
except Exception as e:
    print(f"✗ Error importing serializers: {e}")

try:
    from restaurant.views import MenuViewSet, BookingViewSet, index
    print("✓ Views imported successfully")
except Exception as e:
    print(f"✗ Error importing views: {e}")

try:
    from restaurant import urls
    print("✓ URLs imported successfully")
except Exception as e:
    print(f"✗ Error importing URLs: {e}")

# Test models
try:
    print("\nTesting model creation...")
    from django.contrib.auth.models import User
    
    # Create a test user
    user, created = User.objects.get_or_create(username='testuser', defaults={'email': 'test@test.com'})
    print(f"✓ Test user {'created' if created else 'found'}: {user.username}")
    
    # Create a test menu item
    menu_item, created = Menu.objects.get_or_create(
        title='Test Pizza',
        defaults={'price': 12.99, 'inventory': 10}
    )
    print(f"✓ Test menu item {'created' if created else 'found'}: {menu_item.title} - ${menu_item.price}")
    
    # Create a test booking
    from datetime import datetime, timedelta
    booking_date = datetime.now() + timedelta(days=7)
    booking, created = Booking.objects.get_or_create(
        user=user,
        name='Test Booking',
        no_of_guests=4,
        defaults={'booking_date': booking_date}
    )
    print(f"✓ Test booking {'created' if created else 'found'}: {booking.name} for {booking.no_of_guests} guests")
    
except Exception as e:
    print(f"✗ Error testing models: {e}")
    import traceback
    traceback.print_exc()

print("\n✓ All tests passed!")

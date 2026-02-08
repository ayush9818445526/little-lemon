from django.test import TestCase
from django.contrib.auth.models import User
from .models import Menu, Booking
from datetime import datetime, timedelta


class MenuModelTest(TestCase):
    def setUp(self):
        self.menu = Menu.objects.create(
            title='Pasta Carbonara',
            price=12.99,
            inventory=50
        )

    def test_menu_creation(self):
        self.assertEqual(self.menu.title, 'Pasta Carbonara')
        self.assertEqual(self.menu.price, 12.99)
        self.assertEqual(self.menu.inventory, 50)

    def test_menu_str(self):
        self.assertEqual(str(self.menu), 'Pasta Carbonara')

    def test_menu_price_decimal(self):
        self.assertIsInstance(self.menu.price, type(12.99))

    def test_menu_inventory_default(self):
        menu2 = Menu.objects.create(title='Salad', price=8.99)
        self.assertEqual(menu2.inventory, 0)


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.booking_date = datetime.now() + timedelta(days=7)
        self.booking = Booking.objects.create(
            user=self.user,
            name='John Doe',
            no_of_guests=4,
            booking_date=self.booking_date
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.name, 'John Doe')
        self.assertEqual(self.booking.no_of_guests, 4)
        self.assertEqual(self.booking.user, self.user)

    def test_booking_str(self):
        expected = f'John Doe - {self.booking_date}'
        self.assertEqual(str(self.booking), expected)

    def test_booking_user_relationship(self):
        self.assertEqual(self.booking.user.username, 'testuser')

    def test_booking_delete_cascade(self):
        booking_id = self.booking.id
        self.user.delete()
        self.assertFalse(Booking.objects.filter(id=booking_id).exists())

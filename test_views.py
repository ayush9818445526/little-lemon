from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Menu, Booking
from datetime import datetime, timedelta


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_contains_title(self):
        response = self.client.get('/')
        self.assertContains(response, 'Little Lemon')


class MenuViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(
            title='Pasta',
            price=12.99,
            inventory=50
        )
        self.menu2 = Menu.objects.create(
            title='Salad',
            price=8.99,
            inventory=30
        )

    def test_menu_list(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_menu_retrieve(self):
        response = self.client.get(f'/api/menu/{self.menu1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Pasta')

    def test_menu_create(self):
        data = {
            'title': 'Pizza',
            'price': 14.99,
            'inventory': 40
        }
        response = self.client.post('/api/menu/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 3)

    def test_menu_update(self):
        data = {'title': 'Updated Pasta', 'price': 13.99, 'inventory': 50}
        response = self.client.put(f'/api/menu/{self.menu1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.menu1.refresh_from_db()
        self.assertEqual(self.menu1.title, 'Updated Pasta')

    def test_menu_delete(self):
        response = self.client.delete(f'/api/menu/{self.menu1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 1)


class BookingViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
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

    def test_booking_list(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_booking_retrieve(self):
        response = self.client.get(f'/api/bookings/{self.booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'John Doe')

    def test_booking_create(self):
        future_date = datetime.now() + timedelta(days=14)
        data = {
            'user': self.user.id,
            'name': 'Jane Smith',
            'no_of_guests': 2,
            'booking_date': future_date.isoformat()
        }
        response = self.client.post('/api/bookings/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 2)

    def test_booking_update(self):
        future_date = datetime.now() + timedelta(days=21)
        data = {
            'user': self.user.id,
            'name': 'Updated Name',
            'no_of_guests': 6,
            'booking_date': future_date.isoformat()
        }
        response = self.client.put(f'/api/bookings/{self.booking.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_booking_delete(self):
        response = self.client.delete(f'/api/bookings/{self.booking.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Booking.objects.count(), 0)

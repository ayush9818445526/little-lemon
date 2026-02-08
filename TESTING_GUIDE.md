# API Testing Guide - Little Lemon Capstone

## 🧪 Testing with cURL Commands

### 1. Get Homepage
```bash
curl http://localhost:8000/
```

### 2. List All Menu Items
```bash
curl http://localhost:8000/api/menu/
```

### 3. Create a Menu Item
```bash
curl -X POST http://localhost:8000/api/menu/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Greek Salad",
    "price": "12.99",
    "inventory": 50
  }'
```

### 4. Get Single Menu Item (replace {id} with actual ID)
```bash
curl http://localhost:8000/api/menu/1/
```

### 5. Update Menu Item
```bash
curl -X PUT http://localhost:8000/api/menu/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Updated Greek Salad",
    "price": "13.99",
    "inventory": 45
  }'
```

### 6. Delete Menu Item
```bash
curl -X DELETE http://localhost:8000/api/menu/1/
```

### 7. List All Bookings
```bash
curl http://localhost:8000/api/bookings/
```

### 8. Create a Booking
```bash
curl -X POST http://localhost:8000/api/bookings/ \
  -H "Content-Type: application/json" \
  -d '{
    "user": 1,
    "name": "John Doe",
    "no_of_guests": 4,
    "booking_date": "2026-02-15T19:00:00Z"
  }'
```

### 9. Get Djoser Auth Token
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password"
  }'
```

### 10. Get JWT Token
```bash
curl -X POST http://localhost:8000/api/token/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password"
  }'
```

### 11. API Token Auth Endpoint
```bash
curl -X POST http://localhost:8000/api/api-token-auth/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "your_username",
    "password": "your_password"
  }'
```

---

## 📱 Testing with Insomnia

### Setup Steps:
1. Open Insomnia
2. Create a new Request Collection named "Little Lemon API"
3. Set base URL: `http://localhost:8000`

### Import as Insomnia Collection (JSON)
```json
{
  "name": "Little Lemon API",
  "requests": [
    {
      "method": "GET",
      "url": "http://localhost:8000/",
      "name": "Get Homepage"
    },
    {
      "method": "GET",
      "url": "http://localhost:8000/api/menu/",
      "name": "List Menu Items"
    },
    {
      "method": "POST",
      "url": "http://localhost:8000/api/menu/",
      "name": "Create Menu Item",
      "headers": {
        "Content-Type": "application/json"
      },
      "body": {
        "title": "Pizza Margherita",
        "price": "14.99",
        "inventory": 30
      }
    },
    {
      "method": "GET",
      "url": "http://localhost:8000/api/bookings/",
      "name": "List Bookings"
    },
    {
      "method": "POST",
      "url": "http://localhost:8000/api/bookings/",
      "name": "Create Booking",
      "headers": {
        "Content-Type": "application/json"
      },
      "body": {
        "user": 1,
        "name": "Jane Smith",
        "no_of_guests": 2,
        "booking_date": "2026-02-20T18:30:00Z"
      }
    },
    {
      "method": "POST",
      "url": "http://localhost:8000/api/api-token-auth/",
      "name": "Get Token Auth",
      "headers": {
        "Content-Type": "application/json"
      },
      "body": {
        "username": "admin",
        "password": "your_password"
      }
    },
    {
      "method": "GET",
      "url": "http://localhost:8000/admin/",
      "name": "Django Admin"
    }
  ]
}
```

---

## 🌐 Testing through Browsable API

1. Start the server:
   ```bash
   python manage.py runserver
   ```

2. Open browser and navigate to:
   - **Homepage**: http://localhost:8000/
   - **API Root**: http://localhost:8000/api/
   - **Menu API**: http://localhost:8000/api/menu/
   - **Bookings API**: http://localhost:8000/api/bookings/
   - **Admin Panel**: http://localhost:8000/admin/
   - **Djoser Auth**: http://localhost:8000/api/auth/login/
   - **JWT Auth**: http://localhost:8000/api/token/login/

3. Using the Browsable API:
   - View data in JSON or HTML format
   - Use the form interface to POST/PUT/PATCH/DELETE
   - Authentication works through the browser session

---

## 🧪 Run Unit Tests

### Run all tests:
```bash
python manage.py test restaurant -v 2
```

### Run only model tests:
```bash
python manage.py test restaurant.test_models -v 2
```

### Run only view tests:
```bash
python manage.py test restaurant.test_views -v 2
```

### Run with coverage:
```bash
coverage run --source='restaurant' manage.py test restaurant
coverage report
coverage html
```

---

## 📊 Expected Test Results

### Model Tests (8 tests):
- ✓ Menu creation
- ✓ Menu string representation
- ✓ Menu price validation
- ✓ Menu inventory default
- ✓ Booking creation
- ✓ Booking string representation
- ✓ Booking user relationship
- ✓ Booking cascade delete

### View Tests (12 tests):
- ✓ Index page loads
- ✓ Index contains title
- ✓ Menu list endpoint
- ✓ Menu retrieve endpoint
- ✓ Menu create endpoint
- ✓ Menu update endpoint
- ✓ Menu delete endpoint
- ✓ Booking list endpoint
- ✓ Booking retrieve endpoint
- ✓ Booking create endpoint
- ✓ Booking update endpoint
- ✓ Booking delete endpoint

---

## ✅ Verification Checklist

Before going live, verify:

- [ ] All environment variables in .env are set correctly
- [ ] MySQL database is running and accessible
- [ ] Migrations have been applied successfully
- [ ] Superuser account has been created
- [ ] Sample data has been loaded
- [ ] All unit tests pass
- [ ] Homepage loads correctly
- [ ] API endpoints are accessible
- [ ] Browsable API interface works
- [ ] Admin panel is accessible
- [ ] Token authentication works
- [ ] CORS is configured (if needed)

---

## 🔧 Troubleshooting

### "No database tables exist"
```bash
python manage.py migrate --run-syncdb
```

### "Models haven't been installed yet"
```bash
python manage.py check
```

### "Permission denied" on migrations
```bash
python manage.py migrate --fake-initial
```

### "Connection refused" for database
- Check MySQL is running
- Verify .env DATABASE_* variables
- Test connection: `mysql -h localhost -u root -p`

---

## 📚 Documentation

For more information:
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Djoser](https://djoser.readthedocs.io/)
- [Django Migrations](https://docs.djangoproject.com/en/stable/topics/migrations/)
- [MySQL Python Connector](https://mysqlclient.readthedocs.io/)

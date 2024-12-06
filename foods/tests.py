from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Food
from .forms import FoodForm
from datetime import date, time

class FoodModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.food = Food.objects.create(
            user=self.user,
            date=date.today(),
            eaten_at=timezone.now().time(),
            meal_type='breakfast',
            food_name='Test Food',
            portion_size='medium',
            discomfort='2',
            is_trigger='unsure',
            notes='Test food notes'
        )

    def test_food_creation(self):
        """Test food model creation and string representation"""
        self.assertEqual(str(self.food), "breakfast - Test Food")
        self.assertEqual(self.food.user, self.user)
        self.assertEqual(self.food.meal_type, 'breakfast')
        self.assertEqual(self.food.get_meal_type_display(), 'Breakfast')
        self.assertEqual(self.food.food_name, 'Test Food')
        self.assertEqual(self.food.portion_size, 'medium')
        self.assertEqual(self.food.discomfort, '2')
        self.assertEqual(self.food.is_trigger, 'unsure')

    def test_food_ordering(self):
        """Test foods are ordered by date and eaten_at time descending"""
        yesterday = timezone.now().date() - timezone.timedelta(days=1)
        earlier_time = timezone.now().time().replace(hour=8, minute=0)
        later_time = timezone.now().time().replace(hour=9, minute=0)
        
        food1 = Food.objects.create(
            user=self.user,
            date=yesterday,
            eaten_at=later_time,
            meal_type='lunch',
            food_name='Old Food',
            portion_size='small',
            discomfort='1',
            is_trigger='no'
        )
        
        food2 = Food.objects.create(
            user=self.user,
            date=date.today(),
            eaten_at=earlier_time,
            meal_type='breakfast',
            food_name='Recent Food',
            portion_size='large',
            discomfort='3',
            is_trigger='yes'
        )
        
        foods = Food.objects.all()
        self.assertEqual(foods[0].date, date.today())
        self.assertTrue(foods[0].eaten_at > foods[1].eaten_at)

    def test_future_date_validation(self):
        """Test that future dates are not allowed"""
        future_date = timezone.now().date() + timezone.timedelta(days=1)
        future_food = Food(
            user=self.user,
            date=future_date,
            eaten_at=timezone.now().time(),
            meal_type='lunch',
            food_name='Future Food',
            portion_size='medium',
            discomfort='0',
            is_trigger='no'
        )
        with self.assertRaises(ValidationError):
            future_food.full_clean()

    def test_valid_choices(self):
        """Test that only valid choices are allowed"""
        with self.assertRaises(ValidationError):
            invalid_food = Food(
                user=self.user,
                date=date.today(),
                eaten_at=timezone.now().time(),
                meal_type='invalid_meal',  # Invalid choice
                food_name='Test Food',
                portion_size='medium',
                discomfort='6',  # Invalid choice
                is_trigger='maybe'  # Invalid choice
            )
            invalid_food.full_clean()

class FoodViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.food = Food.objects.create(
            user=self.user,
            date=date.today(),
            eaten_at=timezone.now().time(),
            meal_type='breakfast',
            food_name='Test Food',
            portion_size='medium',
            discomfort='2',
            is_trigger='unsure',
            notes='Test food notes'
        )
        
        self.list_url = reverse('foods:list')
        self.add_url = reverse('foods:add')
        self.edit_url = reverse('foods:edit', args=[self.food.pk])
        self.delete_url = reverse('foods:delete', args=[self.food.pk])

    def test_login_required(self):
        """Test all views require login"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 302)  # Redirects to login
        
        response = self.client.get(self.add_url)
        self.assertEqual(response.status_code, 302)
        
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 302)
        
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 302)

    def test_list_view(self):
        """Test food list view"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'foods/list.html')
        self.assertContains(response, 'Test Food')
        self.assertEqual(len(response.context['foods']), 1)

    def test_add_food(self):
        """Test adding a new food entry"""
        self.client.login(username='testuser', password='testpass123')
        
        # Test GET request
        response = self.client.get(self.add_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'foods/add.html')
        
        # Test POST request
        current_time = timezone.now().time()
        response = self.client.post(self.add_url, {
            'date': date.today(),
            'eaten_at': current_time,
            'meal_type': 'lunch',
            'food_name': 'New Test Food',
            'portion_size': 'large',
            'discomfort': '3',
            'is_trigger': 'yes',
            'notes': 'New test food notes'
        })
        
        self.assertEqual(response.status_code, 302)  # Redirects on success
        self.assertEqual(Food.objects.count(), 2)
        new_food = Food.objects.filter(food_name='New Test Food').first()
        self.assertIsNotNone(new_food)
        self.assertEqual(new_food.meal_type, 'lunch')
        self.assertEqual(new_food.discomfort, '3')
        self.assertEqual(new_food.is_trigger, 'yes')

    def test_edit_food(self):
        """Test editing an existing food entry"""
        self.client.login(username='testuser', password='testpass123')
        
        # Test GET request
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'foods/edit.html')
        
        # Test POST request
        response = self.client.post(self.edit_url, {
            'date': date.today(),
            'eaten_at': self.food.eaten_at,
            'meal_type': 'dinner',
            'food_name': 'Updated Food',
            'portion_size': 'small',
            'discomfort': '4',
            'is_trigger': 'no',
            'notes': 'Updated notes'
        })
        
        self.assertEqual(response.status_code, 302)  # Redirects on success
        updated_food = Food.objects.get(pk=self.food.pk)
        self.assertEqual(updated_food.meal_type, 'dinner')
        self.assertEqual(updated_food.food_name, 'Updated Food')
        self.assertEqual(updated_food.discomfort, '4')
        self.assertEqual(updated_food.is_trigger, 'no')

    def test_delete_food(self):
        """Test deleting a food entry"""
        self.client.login(username='testuser', password='testpass123')
        
        # Test GET request (confirmation page)
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'foods/delete.html')
        
        # Test POST request (actual deletion)
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)  # Redirects on success
        self.assertEqual(Food.objects.count(), 0)

class FoodFormTests(TestCase):
    def test_valid_form(self):
        """Test form with valid data"""
        form_data = {
            'date': date.today(),
            'eaten_at': timezone.now().time(),
            'meal_type': 'breakfast',
            'food_name': 'Test Food',
            'portion_size': 'medium',
            'discomfort': '2',
            'is_trigger': 'unsure',
            'notes': 'Test notes'
        }
        form = FoodForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test form with invalid data"""
        # Test with future date
        form_data = {
            'date': date.today() + timezone.timedelta(days=1),
            'eaten_at': timezone.now().time(),
            'meal_type': 'breakfast',
            'food_name': 'Test Food',
            'portion_size': 'medium',
            'discomfort': '2',
            'is_trigger': 'unsure'
        }
        form = FoodForm(data=form_data)
        self.assertFalse(form.is_valid())
        
        # Test with invalid choices
        form_data = {
            'date': date.today(),
            'eaten_at': timezone.now().time(),
            'meal_type': 'invalid_meal',
            'food_name': 'Test Food',
            'portion_size': 'medium',
            'discomfort': '6',
            'is_trigger': 'maybe'
        }
        form = FoodForm(data=form_data)
        self.assertFalse(form.is_valid())
        
        # Test with missing required fields
        form_data = {
            'notes': 'Test notes'
        }
        form = FoodForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(len(form.errors) >= 7)  # All fields except notes are required

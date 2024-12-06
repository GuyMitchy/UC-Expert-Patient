from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Symptom
from .forms import SymptomForm
from datetime import date

class SymptomModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.symptom = Symptom.objects.create(
            user=self.user,
            type='pain',
            severity=3,
            date=date.today(),
            description='Test symptom description'
        )

    def test_symptom_creation(self):
        """Test symptom model creation and string representation"""
        self.assertEqual(str(self.symptom), 
                    f"Abdominal Pain - Moderate ({self.symptom.date})")
        self.assertEqual(self.symptom.user, self.user)
        self.assertEqual(self.symptom.type, 'pain')
        self.assertEqual(self.symptom.severity, 3)
        self.assertEqual(self.symptom.description, 'Test symptom description')

    def test_symptom_ordering(self):
        """Test symptoms are ordered by date descending"""
        yesterday = timezone.now().date() - timezone.timedelta(days=1)
        older_symptom = Symptom.objects.create(
            user=self.user,
            type='fatigue',
            severity=2,
            date=yesterday
        )
        symptoms = Symptom.objects.all()
        self.assertEqual(symptoms[0], self.symptom)  # Most recent first
        self.assertEqual(symptoms[1], older_symptom)

    def test_future_date_validation(self):
        """Test that future dates are not allowed"""
        future_date = timezone.now().date() + timezone.timedelta(days=1)
        future_symptom = Symptom(
            user=self.user,
            type='pain',
            severity=3,
            date=future_date
        )
        # Use full_clean() to trigger validation
        with self.assertRaises(ValidationError):
            future_symptom.full_clean()

class SymptomViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.symptom = Symptom.objects.create(
            user=self.user,
            type='pain',
            severity=3,
            date=date.today(),
            description='Test symptom description'
        )
        self.list_url = reverse('symptoms:list')
        self.add_url = reverse('symptoms:add')
        self.edit_url = reverse('symptoms:edit', args=[self.symptom.pk])
        self.delete_url = reverse('symptoms:delete', args=[self.symptom.pk])

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
        """Test symptom list view"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'symptoms/list.html')
        self.assertContains(response, 'Test symptom description')
        self.assertEqual(len(response.context['symptoms']), 1)

    def test_add_symptom(self):
        """Test adding a new symptom"""
        self.client.login(username='testuser', password='testpass123')
        
        # Test GET request
        response = self.client.get(self.add_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'symptoms/add.html')
        
        # Test POST request
        response = self.client.post(self.add_url, {
            'type': 'blood',
            'severity': 4,
            'date': date.today(),
            'description': 'New test symptom'
        })
        
        self.assertEqual(response.status_code, 302)  # Redirects on success
        self.assertEqual(Symptom.objects.count(), 2)
        new_symptom = Symptom.objects.filter(type='blood').first()
        self.assertIsNotNone(new_symptom)
        self.assertEqual(new_symptom.type, 'blood')
        self.assertEqual(new_symptom.severity, 4)

    def test_edit_symptom(self):
        """Test editing an existing symptom"""
        self.client.login(username='testuser', password='testpass123')
        
        # Test GET request
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'symptoms/edit.html')
        
        # Test POST request
        response = self.client.post(self.edit_url, {
            'type': 'fatigue',
            'severity': 2,
            'date': date.today(),
            'description': 'Updated description'
        })
        
        self.assertEqual(response.status_code, 302)  # Redirects on success
        updated_symptom = Symptom.objects.get(pk=self.symptom.pk)
        self.assertEqual(updated_symptom.type, 'fatigue')
        self.assertEqual(updated_symptom.severity, 2)
        self.assertEqual(updated_symptom.description, 'Updated description')

    def test_delete_symptom(self):
        """Test deleting a symptom"""
        self.client.login(username='testuser', password='testpass123')
        
        # Test GET request (confirmation page)
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'symptoms/delete.html')
        
        # Test POST request (actual deletion)
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)  # Redirects on success
        self.assertEqual(Symptom.objects.count(), 0)

class SymptomFormTests(TestCase):
    def test_valid_form(self):
        """Test form with valid data"""
        form_data = {
            'type': 'pain',
            'severity': 3,
            'date': date.today(),
            'description': 'Test description'
        }
        form = SymptomForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test form with invalid data"""
        # Test with future date
        form_data = {
            'type': 'pain',
            'severity': 3,
            'date': date.today() + timezone.timedelta(days=1),
            'description': 'Test description'
        }
        form = SymptomForm(data=form_data)
        self.assertFalse(form.is_valid())
        
        # Test with missing required fields
        form_data = {
            'description': 'Test description'
        }
        form = SymptomForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)  # type, severity, and date are required
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Medication
from .forms import MedicationForm
from datetime import date

class MedicationModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        
        self.medication = Medication.objects.create(
            user=self.user,
            name='MESALAZINE_ORAL',
            dosage='40mg',
            frequency='daily',
            start_date=date.today(),
            active=True,
            notes='Test medication notes'
        )

    def test_medication_creation(self):
        """Test medication model creation and string representation"""
        self.assertEqual(str(self.medication), 
                       f"Mesalazine (Oral) - 40mg")
        self.assertEqual(self.medication.user, self.user)
        self.assertEqual(self.medication.get_name_display(), 'Mesalazine (Oral)')
        self.assertEqual(self.medication.dosage, '40mg')
        self.assertEqual(self.medication.get_frequency_display(), 'Daily')
        self.assertTrue(self.medication.active)

    def test_medication_ordering(self):
        """Test medications are ordered by active status and start_date"""
        yesterday = timezone.now().date() - timezone.timedelta(days=1)
        inactive_med = Medication.objects.create(
            user=self.user,
            name='PREDNISOLONE',
            dosage='20mg',
            frequency='daily',
            start_date=yesterday,
            active=False
        )
        medications = Medication.objects.all()
        self.assertEqual(medications[0], self.medication)  # Active medication first
        self.assertEqual(medications[1], inactive_med)

    def test_future_date_validation(self):
        """Test that future start dates are not allowed"""
        future_date = timezone.now().date() + timezone.timedelta(days=1)
        future_med = Medication(
            user=self.user,
            name='PREDNISOLONE',
            dosage='20mg',
            frequency='daily',
            start_date=future_date,
            active=True
        )
        with self.assertRaises(ValidationError):
            future_med.full_clean()

    def test_valid_choices(self):
        """Test that only valid choices are allowed"""
        with self.assertRaises(ValidationError):
            invalid_med = Medication(
                user=self.user,
                name='INVALID_MED',  # Invalid choice
                dosage='20mg',
                frequency='invalid_freq',  # Invalid choice
                start_date=date.today(),
                active=True
            )
            invalid_med.full_clean()

class MedicationViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.medication = Medication.objects.create(
            user=self.user,
            name='MESALAZINE_ORAL',
            dosage='40mg',
            frequency='daily',
            start_date=date.today(),
            active=True,
            notes='Test medication notes'
        )
        self.list_url = reverse('medications:list')
        self.add_url = reverse('medications:add')
        self.edit_url = reverse('medications:edit', args=[self.medication.pk])
        self.delete_url = reverse('medications:delete', args=[self.medication.pk])

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
        """Test medication list view"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medications/list.html')
        self.assertContains(response, 'Mesalazine (Oral)')
        self.assertContains(response, '40mg')
        self.assertEqual(len(response.context['medications']), 1)

    def test_add_medication(self):
        """Test adding a new medication"""
        self.client.login(username='testuser', password='testpass123')
        
        # Test GET request
        response = self.client.get(self.add_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medications/add.html')
        
        # Test POST request
        response = self.client.post(self.add_url, {
            'name': 'PREDNISOLONE',
            'dosage': '20mg',
            'frequency': 'twice_daily',
            'start_date': date.today(),
            'active': True,
            'notes': 'New test medication'
        })
        
        self.assertEqual(response.status_code, 302)  # Redirects on success
        self.assertEqual(Medication.objects.count(), 2)
        new_med = Medication.objects.filter(name='PREDNISOLONE').first()
        self.assertIsNotNone(new_med)
        self.assertEqual(new_med.dosage, '20mg')
        self.assertEqual(new_med.get_frequency_display(), 'Twice Daily')

    def test_edit_medication(self):
        """Test editing an existing medication"""
        self.client.login(username='testuser', password='testpass123')
        
        # Test GET request
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medications/edit.html')
        
        # Test POST request
        response = self.client.post(self.edit_url, {
            'name': 'PREDNISOLONE',
            'dosage': '30mg',
            'frequency': 'daily',
            'start_date': date.today(),
            'active': False,
            'notes': 'Updated notes'
        })
        
        self.assertEqual(response.status_code, 302)  # Redirects on success
        updated_med = Medication.objects.get(pk=self.medication.pk)
        self.assertEqual(updated_med.name, 'PREDNISOLONE')
        self.assertEqual(updated_med.dosage, '30mg')
        self.assertFalse(updated_med.active)
        self.assertEqual(updated_med.notes, 'Updated notes')

    def test_delete_medication(self):
        """Test deleting a medication"""
        self.client.login(username='testuser', password='testpass123')
        
        # Test GET request (confirmation page)
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'medications/delete.html')
        
        # Test POST request (actual deletion)
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)  # Redirects on success
        self.assertEqual(Medication.objects.count(), 0)

class MedicationFormTests(TestCase):
    def test_valid_form(self):
        """Test form with valid data"""
        form_data = {
            'name': 'MESALAZINE_ORAL',
            'dosage': '40mg',
            'frequency': 'daily',
            'start_date': date.today(),
            'active': True,
            'notes': 'Test notes'
        }
        form = MedicationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test form with invalid data"""
        # Test with future date
        form_data = {
            'name': 'MESALAZINE_ORAL',
            'dosage': '40mg',
            'frequency': 'daily',
            'start_date': date.today() + timezone.timedelta(days=1),
            'active': True
        }
        form = MedicationForm(data=form_data)
        self.assertFalse(form.is_valid())
        
        # Test with invalid choices
        form_data = {
            'name': 'INVALID_MED',
            'dosage': '40mg',
            'frequency': 'invalid_freq',
            'start_date': date.today(),
            'active': True
        }
        form = MedicationForm(data=form_data)
        self.assertFalse(form.is_valid())
        
        # Test with missing required fields
        form_data = {
            'notes': 'Test notes'
        }
        form = MedicationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(len(form.errors) >= 4)  # name, dosage, frequency, start_date are required
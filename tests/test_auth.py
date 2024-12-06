from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from allauth.account.models import EmailAddress


class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('account_signup')
        self.login_url = reverse('account_login')
        self.logout_url = reverse('account_logout')
        self.home_url = reverse('home:home')

        # Create a test user with auto-generated username from email
        self.user = get_user_model().objects.create_user(
            username='testuser@example.com',  # Using email as username
            email='testuser@example.com',
            password='testpass123'
        )
        EmailAddress.objects.create(
            user=self.user,
            email=self.user.email,
            primary=True,
            verified=True
        )

    def test_signup_page(self):
        """Test signup page loads correctly"""
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_user_signup(self):
        """Test user registration process"""
        response = self.client.post(self.signup_url, {
            'email': 'newuser@example.com',
            'password1': 'newuserpass123',
            'password2': 'newuserpass123',
        })

        # Should redirect after successful signup
        self.assertEqual(response.status_code, 302)

        # Verify user was created
        self.assertTrue(
            get_user_model().objects.filter(email='newuser@example.com').
            exists()
        )

        # Verify email address was created
        self.assertTrue(
            EmailAddress.objects.filter(email='newuser@example.com').exists()
        )

    def test_login_page(self):
        """Test login page loads correctly"""
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_user_login(self):
        """Test user login process"""
        response = self.client.post(self.login_url, {
            'login': 'testuser@example.com',
            'password': 'testpass123'
        })

        # Should redirect after successful login
        self.assertEqual(response.status_code, 302)

        # Verify user is logged in
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_user_logout(self):
        """Test user logout process"""
        # First login
        self.client.login(
                        username='testuser@example.com', password='testpass123'
                        )

        # Then logout
        response = self.client.post(self.logout_url)

        # Should redirect after logout
        self.assertEqual(response.status_code, 302)

        # Verify user is logged out
        response = self.client.get(self.home_url)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_password_change(self):
        """Test password change functionality"""
        self.client.login(
                        username='testuser@example.com', password='testpass123'
                        )

        response = self.client.post(reverse('account_change_password'), {
            'oldpassword': 'testpass123',
            'password1': 'newtestpass123',
            'password2': 'newtestpass123'
        })

        # Should redirect after password change
        self.assertEqual(response.status_code, 302)

        # Verify can login with new password
        self.client.logout()
        login_successful = self.client.login(
            username='testuser@example.com',
            password='newtestpass123'
        )
        self.assertTrue(login_successful)

    def test_invalid_login(self):
        """Test login with invalid credentials"""
        response = self.client.post(self.login_url, {
            'login': 'testuser@example.com',
            'password': 'wrongpassword'
        })

        # Should stay on login page
        self.assertEqual(response.status_code, 200)

        # Should show error message
        self.assertContains(response,
                            "The email address and/or password you"
                            "specified are not correct")

    def test_signup_password_validation(self):
        """Test password validation during signup"""
        # Test too short password
        response = self.client.post(self.signup_url, {
            'email': 'newuser@example.com',
            'password1': 'short',
            'password2': 'short',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This password is too short")

        # Test common password
        response = self.client.post(self.signup_url, {
            'email': 'newuser@example.com',
            'password1': 'password123',
            'password2': 'password123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This password is too common")

        # Test password mismatch
        response = self.client.post(self.signup_url, {
            'email': 'newuser@example.com',
            'password1': 'validpass123',
            'password2': 'differentpass123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response,
                            "You must type the same password each time")

    def test_email_required(self):
        """Test email is required for signup"""
        response = self.client.post(self.signup_url, {
            'email': '',
            'password1': 'testpass123',
            'password2': 'testpass123',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required")

    def test_authenticated_user_redirect(self):
        """Test authenticated users are redirected from login/signup pages"""
        # Login first
        self.client.login(
            username='testuser@example.com',
            password='testpass123'
            )

        # Try accessing login page
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 302)

        # Try accessing signup page
        response = self.client.get(self.signup_url)
        self.assertEqual(response.status_code, 302)

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from unittest.mock import patch
from .models import Conversation, Message


class ChatModelTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

        self.conversation = Conversation.objects.create(
            user=self.user,
            title='Test Conversation'
        )

        self.message = Message.objects.create(
            conversation=self.conversation,
            content='Hello, this is a test message',
            is_bot=False
        )

    def test_conversation_creation(self):
        """Test conversation model creation and string representation"""
        self.assertEqual(
            str(self.conversation),
            f"Conversation Test Conversation - {self.user.username}"
        )
        self.assertEqual(self.conversation.user, self.user)
        self.assertEqual(self.conversation.title, 'Test Conversation')
        self.assertIsNotNone(self.conversation.created_at)
        self.assertIsNotNone(self.conversation.updated_at)

    def test_message_creation(self):
        """Test message model creation and string representation"""
        self.assertEqual(
            str(self.message),
            "User: Hello, this is a test message..."
        )
        self.assertEqual(self.message.conversation, self.conversation)
        self.assertEqual(self.message.content, 'Hello, this is a test message')
        self.assertFalse(self.message.is_bot)
        self.assertIsNotNone(self.message.created_at)

    def test_conversation_ordering(self):
        """Test conversations are ordered by updated_at"""
        older_conversation = Conversation.objects.create(
            user=self.user,
            title='Older Conversation'
        )
        # Force update of updated_at
        self.conversation.save()

        conversations = Conversation.objects.all()
        self.assertEqual(conversations[0], self.conversation)
        self.assertEqual(conversations[1], older_conversation)

    def test_message_ordering(self):
        """Test messages are ordered by created_at"""
        new_message = Message.objects.create(
            conversation=self.conversation,
            content='A newer message',
            is_bot=True
        )

        messages = Message.objects.all()
        self.assertEqual(messages[0], self.message)
        self.assertEqual(messages[1], new_message)

    def test_conversation_get_absolute_url(self):
        """Test get_absolute_url method"""
        expected_url = reverse(
            'chat:detail', kwargs={'pk': self.conversation.pk}
            )
        self.assertEqual(
            self.conversation.get_absolute_url(), expected_url
            )


class ChatViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

        self.conversation = Conversation.objects.create(
            user=self.user,
            title='Test Conversation'
        )

        self.message = Message.objects.create(
            conversation=self.conversation,
            content='Test message',
            is_bot=False
        )

        self.list_url = reverse('chat:list')
        self.create_url = reverse('chat:new')
        self.detail_url = reverse('chat:detail', args=[self.conversation.pk])
        self.delete_url = reverse('chat:delete', args=[self.conversation.pk])
        self.send_message_url = reverse(
            'chat:send_message',
            args=[self.conversation.pk]
        )

    def test_login_required(self):
        """Test all views require login"""
        urls = [
            self.list_url,
            self.create_url,
            self.detail_url,
            self.delete_url,
            self.send_message_url
        ]

        for url in urls:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)  # Redirects to login

    def test_list_view(self):
        """Test conversation list view"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/list.html')
        self.assertContains(response, 'Test Conversation')
        self.assertEqual(len(response.context['conversations']), 1)

    def test_create_conversation(self):
        """Test creating a new conversation"""
        self.client.login(username='testuser', password='testpass123')

        # Test GET request
        response = self.client.get(self.create_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/new_conversation.html')

        # Test POST request
        response = self.client.post(self.create_url, {
            'title': 'New Conversation'
        })

        self.assertEqual(response.status_code, 302)  # Redirects on success
        self.assertEqual(Conversation.objects.count(), 2)
        new_conversation = Conversation.objects.get(title='New Conversation')

        # Verify welcome message was created
        welcome_message = Message.objects.filter(
            conversation=new_conversation,
            is_bot=True).first()
        self.assertIsNotNone(welcome_message)
        self.assertTrue("I'm your UC Expert assistant"
                        in welcome_message.content)

    def test_detail_view(self):
        """Test conversation detail view"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/detail.html')
        self.assertContains(response, 'Test Conversation')
        self.assertContains(response, 'Test message')
        self.assertEqual(response.context['conversation'], self.conversation)

    def test_delete_conversation(self):
        """Test deleting a conversation"""
        self.client.login(username='testuser', password='testpass123')

        # Test GET request (confirmation page)
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/delete.html')

        # Test POST request (actual deletion)
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)  # Redirects on success
        self.assertEqual(Conversation.objects.count(), 0)
        # Verify messages are also deleted
        self.assertEqual(Message.objects.count(), 0)

    @patch('knowledge.manager.UCExpertRAG')
    def test_send_message(self, mock_rag):
        """Test sending a message (with mocked RAG)"""
        # Configure mock
        mock_rag_instance = mock_rag.return_value
        mock_rag_instance.get_response.return_value = "Mocked bot response"

        self.client.login(username='testuser', password='testpass123')

        response = self.client.post(self.send_message_url, {
            'message': 'Test user message'
        })

        self.assertEqual(response.status_code, 200)

        # Verify user message was created
        user_message = Message.objects.filter(
            conversation=self.conversation,
            content='Test user message',
            is_bot=False
        ).exists()
        self.assertTrue(user_message)

        # Verify bot response was created
        bot_message = Message.objects.filter(
            conversation=self.conversation,
            content='Mocked bot response',
            is_bot=True
        ).exists()
        self.assertTrue(bot_message)

    def test_user_can_only_access_own_conversations(self):
        """Test users can only access their own conversations"""
        other_user = get_user_model().objects.create_user(
            username='otheruser',
            email='other@example.com',
            password='otherpass123'
        )
        other_conversation = Conversation.objects.create(
            user=other_user,
            title='Other Conversation'
        )

        self.client.login(username='testuser', password='testpass123')

        # Try to access other user's conversation
        response = self.client.get(
            reverse('chat:detail', args=[other_conversation.pk])
        )
        self.assertEqual(response.status_code, 404)

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, reverse_lazy

from main.models import Email


class EmailTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='password',
        )

        self.email = Email.objects.create(
            topic='topic',
            text='text',
            sender=self.user,
        )

    def test_string_representation(self):
        email = Email(topic='topic')
        self.assertEqual(str(email), email.topic)

    def test_email_content(self):
        self.assertEqual(f'{self.email.topic}', 'topic')
        self.assertEqual(f'{self.email.sender}', 'testuser')
        self.assertEqual(f'{self.email.text}', 'text')

    def test_email_list_view(self):
        response = self.client.get(reverse('inbox'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'text')
        self.assertTemplateUsed(response, 'main/inbox_list.html')

    def test_email_detail_view(self):
        response = self.client.get(reverse('inbox'))
        no_response = self.client.get('/email/19823/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'topic')
        self.assertTemplateUsed(response, 'main/inbox_list.html')

    def test_email_delete_view(self):
        response = self.client.post(
            reverse('email-delete', args='6'))
        self.assertEqual(response.status_code, 302)

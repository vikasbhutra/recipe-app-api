from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin = get_user_model().objects.create_super_user(
            email="admin@gmail.com",
            password="pass123"
        )
        self.client.force_login(self.admin)

        self.user = get_user_model().objects.create_user(
            email="user@gmail.com",
            password="passs23",
            name="vikas"
        )

    def test_users_listed(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

from django.test import TestCase
from django.contrib.auth import get_user_model


class Test_Models(TestCase):

    def test_create_user_models_with_email_successful(self):
        '''
            Test for creating a new user with email is successful
        '''
        email = "xyz@gmail.com"
        password = "testpass"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_user_model_with_normalised_mail(self):
        '''Test for creating new user with normalised email'''

        email = "xyz@GMAIL.COM"
        password = "testpass"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email.lower())

    def test_create_user_model_rasies_error_with_noemail(self):
        '''Test for creating new user with no email id'''
        with self.assertRaises(ValueError):
            user = get_user_model().objects.create_user(email="")

    def test_create_super_user(self):
        '''Test for creating new super user'''
        email = "axz@gmail.com"
        password = "testpass"
        user = get_user_model().objects.create_super_user(email=email, password=password)
        print(user)
        self.assertEqual(user.email, email)
        self.assertTrue(user.is_superuser)

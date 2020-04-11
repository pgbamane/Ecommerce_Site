from django.contrib.auth import get_user_model
from django.test import TestCase


class UserManagerTestCase(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(first_name='Pradnya',
                                        last_name='Bamane',
                                        email_id='pradnya@gmail.com',
                                        phone_number='9545065515',
                                        gender='female',
                                        )
        self.assertEqual(user.first_name, 'Pradnya')
        self.assertEqual(user.last_name, 'Bamane')
        self.assertEqual(user.email_id, 'pradnya@gmail.com')
        self.assertEqual(user.get_username(), user.email_id)

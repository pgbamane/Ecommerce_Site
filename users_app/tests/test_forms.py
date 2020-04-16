from django import test

from users_app.forms import SignupForm


class SignupFormTestCase(test.TestCase):
    def test_signup_form_field_errors(self):
        signup_form_data = {
            'first_name': 'Akshay',
            'last_name': 'Satpute',
            'gender': 'male',
            'address': 'satpute male',
            'locality': 'waddi',
            'state': 'Maharashtra',
            'district': 'Sangli',
            'city': 'Miraj',
            'pincode': '416410',
            'phone_number': '7878457845',
            'email': 'akshay@gmail.com',
            'password1': 'satputeps',
            'password2': 'satputeps'
        }
        form = SignupForm(signup_form_data)

        print("\n\nForm Valid:", form.is_valid())
        self.assertTrue(form.is_valid())

        print("\n\nForm errors:", form.errors)
        self.assertEqual(form.errors, {})

        print("\n first_name:", form.cleaned_data['first_name'])

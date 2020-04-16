from django import test
from django.contrib.auth import get_user_model
import json
from django.test import Client, RequestFactory
from django.urls import reverse

from users_app.forms.signupform import SignupForm


class SignupViewTestCase(test.TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

    def setUp(self):
        self.factory = RequestFactory()

    def test_get_request(self):
        response = self.client.get(reverse('account_signup'))
        # print("Path:", response.path)
        self.assertTrue(response.status_code == 200)
        self.assertTemplateUsed(response, 'account/signup.html')
        self.assertFormError(response, 'form', None, [])
        # self.ass

    def test_post_request_form_valid_data(self):
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

        # form = SignupForm({
        #     'first_name': 'Akshay',
        #     'last_name': 'Satpute',
        #     'gender': 'male',
        #     'address': 'satpute male',
        #     'locality': 'waddi',
        #     'state': 'Maharashtra',
        #     'district': 'Sangli',
        #     'city': 'Miraj',
        #     'pincode': '416410',
        #     'phone_number': '7878457845',
        #     'email_id': 'akshay@gmail.com',
        #     'password': 'satputeps'
        # })
        # json_data = json.dumps(sign_up_form_data)
        form = SignupForm(signup_form_data)
        print("\n\nForm Valid:", form.is_valid())
        response = self.client.post(reverse('account_signup'),  # by default sends data in 'multipart/form-data; '
                                    data=signup_form_data,  # json data
                                    # content_type='application/json',
                                    # for ajax request
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(response['content-type'], 'application/json')

        print("\nResponse Status Code:", response.status_code)
        self.assertEqual(response.status_code, 200)

        print("\nResponse Content(String representation) :", response.content)
        # self.assertFormError(response, 'form', None, [])

        print("\n Response Json: ", response.json())
        self.assertTrue(response.json())

        print("\n Response Json Location:", response.json()['location'])
        self.assertEqual(response.json()['location'], reverse('home'))

        print("\n Response Json Form:", response.json()['form'])
        self.assertTrue(response.json()['form'])

        # For invalid form: its is successful same page with form errors load: sucessful page load :status 200
        # for valid form: it will redirect to something ex login page: redirect status code 302
        # print(response.content)
        # print("Ajax:", response.is_ajax())
        # print(form.signup(request, get_user_model()))
        # self.assertEqual(response.status_code, 302)
        # self.assertTrue(get_user_model().objects.filter(first_name='Akshay').exists())
        # self.assertEqual(request.)
        # form.signup(user=get_user_model())

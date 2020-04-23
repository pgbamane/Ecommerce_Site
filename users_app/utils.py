from django.urls import reverse


def custom_signup_redirect(success_url=None):
    # ret = '/whatever/url/?next=' + success_url
    # return ret
    return reverse('account_login')

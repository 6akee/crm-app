from django.test import SimpleTestCase
from django.urls import reverse, resolve
from website.views import home, logout_user, register_user, customer_record


class TestUrls(SimpleTestCase):
    
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func, home)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout_user)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register_user)

    def test_record_url_resolves(self):
        url = reverse('record', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func, customer_record)
from unittesting.apptwo import wishing_user
import unittest
from django.test.client import RequestFactory


class TestOne(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_one(self):
        request = self.factory.get('')
        response = wishing_user(request, 11)
        self.assertEqual(response, 'Good Morning')

    def test_two(self):
        request = self.factory.get('')
        response = wishing_user(request, 15)
        self.assertEqual(response, 'Good Evening')

    def test_three(self):
        request = self.factory.get('')
        response = wishing_user(request, 23)
        self.assertNotEqual(response, "Good Morning")

    def test_four(self):
        request = self.factory.get('')
        response = wishing_user(request, 5)
        self.assertEqual(response, "Good Night")






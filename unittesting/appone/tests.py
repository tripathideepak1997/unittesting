import unittest
from django.test.client import RequestFactory


class testcasetwo(unittest.TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()

    def test_one(self):
        request = self.factory.get('')
        response = read_file(request, 'file')
        self.assertEqual(response.status_code, 200)

    def test_two(self):
        request = self.factory.get('')
        response = read_file(request, 'file_two')
        self.assertNotEqual(response,
                            HttpResponse('no such file found'))

    def test_three(self):
        request = self.factory.delete('')
        response = delete_file(request, 'file_two')
        self.assertEqual(response, HttpResponse('file deleted successfully'))

import unittest

from django.test import TestCase
from django.test import Client


class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # def test_post_detail(self):
    #     response = self.client.get('hhtp://www.google.com')
    #     self.assertEqual(response.status_code, 200)

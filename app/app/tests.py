from django.test import TestCase
import json


class HomePageTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content.decode()), {"hello": "world"})

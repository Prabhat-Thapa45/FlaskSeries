import unittest
import requests
from src.check import check_flower_by_name
from app import app


class TestApi(unittest.TestCase):
    URL = "http://127.0.0.1:5000/"

    def test_home(self):
        tester = app.test_client(self)
        response = tester.get("/home")
        self.assertEqual(response.status_code, 200)

    def test_about(self):
        response = requests.get(self.URL + 'about')
        self.assertEqual(response.status_code, 200)

    def test_contact(self):
        response = requests.get(self.URL + 'contact')
        self.assertEqual(response.status_code, 200)

    def test_menu(self):
        response = requests.get(self.URL + 'menu')
        self.assertEqual(response.status_code, 200)

    def test_bouquet(self):
        """
        asserts if get request is working or not
        then tries for post request with series of different data passed to it
        """
        response = requests.get(self.URL + 'bouquet_size')
        self.assertEqual(response.status_code, 200)
        for i in [1, 3, -3, 0, "", "efe", "2"]:
            response = requests.post(self.URL + 'bouquet_size', data={'bouquet_size': i})
            self.assertEqual(response.status_code, 200)

    def test_add_flower(self):
        """
        asserts if get request is working or not
        then tries for post request with series of different data passed to it
        """
        response = requests.get(self.URL + 'add_flower')
        self.assertEqual(response.status_code, 200)

        for i in [1]:
            response = requests.post(self.URL + 'add_flower', data={'number': i})
            self.assertEqual(response.status_code, 200)






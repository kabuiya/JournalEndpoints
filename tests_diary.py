import unittest
from diary import app, entr
import json

from models import Entries


class TestsDiary(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        self.entry = {"content": "Testing add_entries"}
        self.added_entry = {"content": "Testing add_entries", "id": 0}

    def tearDown(self):
        entr.items = []

    def add_entry(self):
        """
        add entry
        :return:
        """
        response = self.client.post('/api/v1/add', json=self.entry)
        return response

    def test_get_entries(self):
        self.add_entry()
        response = self.client.get('/api/v1/entries')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [self.added_entry])

    def test_add_entries(self):
        response = self.add_entry()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), [self.added_entry])

    def test_get_entry(self):
        self.add_entry()
        response = self.client.get("/api/v1/entry/0")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), self.added_entry)

    def test_update_entry(self):
        """
        tests update entry
        """
        self.add_entry()
        data = {"content": "Testing add_entries updated version 1"}
        res = {"content": "Testing add_entries updated version 1", "id": 0}
        response = self.client.put('/api/v1/update/0', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), [res])


if __name__ == '__main__':
    unittest.main()
#run
import unittest
from unittest.mock import patch
from stats import app

class TestStatsApi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def tearDown(self):
        pass

    @patch("stats.Dna")
    def test_mutant_post_response_false(self, dna):
        response = self.client.get('/stats')
        expected_resp = {'count_mutant_dna':0, 'count_human_dna':0, 'ratio':0}
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.get_json(), expected_resp)

    def test_dummy_get_response(self):
        response = self.client.get('/dummy')
        expected_resp = {'message': 'ok'}
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.get_json(), expected_resp)

    def test_hello_world_get_response(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
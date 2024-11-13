
import unittest
from app.app import app

class FlaskRoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_route(self):
        response = self.app.get('/product/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

import unittest
from src.app import app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_index_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_debug_endpoint(self):
        response = self.app.get('/debug')
        self.assertEqual(response.status_code, 200)
    
    def test_user_endpoint(self):
        response = self.app.get('/users/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
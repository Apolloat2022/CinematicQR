import unittest
import io
from app import create_app

class TestQRGenerator(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_generate_qr_success(self):
        response = self.client.post('/api/generate', json={
            'url': 'https://google.com',
            'fill': '#ff0000'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'image/png')
        self.assertTrue(len(response.data) > 0)

    def test_generate_qr_missing_url(self):
        response = self.client.post('/api/generate', json={
            'fill': '#000000'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('url required', response.get_json()['error'])

if __name__ == '__main__':
    unittest.main()

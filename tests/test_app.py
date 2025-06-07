import unittest
import app.main as app

class TestApp(unittest.TestCase):
    def test_health(self):
        client = app.app.test_client()
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

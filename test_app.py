import unittest
from app import app

class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_home_page(self):

        response = self.client.get("/")

        # Intentionally incorrect
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
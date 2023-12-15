import qr_monkey
import unittest
from unittest.mock import patch
import requests
from qr_monkey import QrCodeMonkeyAPI, base_url

class TestQrCodeMonkeyAPI(unittest.TestCase):
    @patch('requests.post')
    def test_create_custom_qr_code_success(self, mock_post):
        # Arrange
        mock_response = requests.Response()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        qr_api = QrCodeMonkeyAPI()
        params = {
            "data": base_url,
            "config": {
                "body": "circle",
            },
            "size": 300,
            "download": False,
            "file": "png"
        }

        # Act
        result = qr_api.create_custom_qr_code(params)

        # Assert
        self.assertIsNotNone(result)

    @patch('requests.post')
    def test_create_custom_qr_code_failure(self, mock_post):
        # Arrange
        mock_response = requests.Response()
        mock_response.status_code = 404  # Simulating a failure status code
        mock_post.return_value = mock_response

        qr_api = QrCodeMonkeyAPI()
        params = {
            "data": base_url,
            "config": {
                "body": "circle",
            },
            "size": 300,
            "download": False,
            "file": "png"
        }

        # Act
        result = qr_api.create_custom_qr_code(params)

        # Assert
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

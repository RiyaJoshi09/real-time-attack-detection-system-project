import unittest
import json
from app import app, socketio
from flask_socketio import SocketIOTestClient

class RealTimeAttackDetectionTest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.url_analyze = "/analyze"
        self.url_logs = "/logs"
        self.headers = {"Content-Type": "application/json"}

        # Clear any previously stored logs (if you're storing them globally)
        if hasattr(app, "attack_logs"):
            app.attack_logs.clear()

    def send_request(self, payload):
        return self.client.post(
            self.url_analyze,
            headers=self.headers,
            data=json.dumps(payload)
        )

    def test_sql_login_bypass(self):
        payload = {
            "username": "admin",
            "password": "' OR '1'='1"
        }
        response = self.send_request(payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("attack_detected", response.json["status"])

    def test_union_select(self):
        payload = {
            "search": "test' UNION SELECT * FROM users --"
        }
        response = self.send_request(payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("attack_detected", response.json["status"])

    def test_xss_script(self):
        payload = {
            "comment": "<script>alert('Hacked!')</script>"
        }
        response = self.send_request(payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("attack_detected", response.json["status"])

    def test_img_onerror_xss(self):
        payload = {
            "image": "<img src=x onerror=alert('xss')>"
        }
        response = self.send_request(payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("attack_detected", response.json["status"])

    def test_traversal_payload(self):
        payload = {
            "url": "../../../../etc/passwd"
        }
        response = self.send_request(payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("attack_detected", response.json["status"])

    def test_safe_input(self):
        payload = {
            "name": "Alice",
            "comment": "Nice website!"
        }
        response = self.send_request(payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["status"], "clean")

    def test_logs_endpoint_after_attacks(self):
        # Trigger two attacks
        self.send_request({"field": "' OR '1'='1"})
        self.send_request({"comment": "<script>alert('XSS')</script>"})

        # Now check the logs
        logs_response = self.client.get(self.url_logs)
        self.assertEqual(logs_response.status_code, 200)
        logs = logs_response.get_json()

        self.assertIsInstance(logs, list)
        self.assertGreaterEqual(len(logs), 2)
        for log in logs:
            self.assertIn("timestamp", log)
            self.assertIn("ip", log)
            self.assertIn("payload", log)
            self.assertIn("patterns", log)

if __name__ == "__main__":
    unittest.main()

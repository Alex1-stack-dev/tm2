import unittest
from unittest.mock import MagicMock, patch
from utils.logger import log_hardware_io

class TestHardwareIntegration(unittest.TestCase):
    def setUp(self):
        # Mock device setup
        self.device = MagicMock()

    def test_normal_operation(self):
        self.device.send.return_value = "OK"
        response = self.device.send("START")
        log_hardware_io("SEND", "START")
        log_hardware_io("RECV", response)
        self.assertEqual(response, "OK")

    def test_device_unavailable(self):
        self.device.send.side_effect = Exception("Device not found")
        with self.assertRaises(Exception):
            self.device.send("START")
            log_hardware_io("SEND", "START")

    def test_bad_response(self):
        self.device.send.return_value = "??"
        response = self.device.send("READ")
        log_hardware_io("SEND", "READ")
        log_hardware_io("RECV", response)
        self.assertEqual(response, "??")

    def test_timeout(self):
        self.device.send.side_effect = TimeoutError("Timeout waiting for device")
        with self.assertRaises(TimeoutError):
            self.device.send("PING")
            log_hardware_io("SEND", "PING")

    def test_false_start(self):
        # Simulate device flagging a false start
        self.device.send.return_value = "FS"
        resp = self.device.send("CHECK")
        log_hardware_io("SEND", "CHECK")
        log_hardware_io("RECV", resp)
        self.assertEqual(resp, "FS")

    # Add edge/exception tests: missed touch, tie, etc.

if __name__ == '__main__':
    unittest.main()

from controllers.base_controller import SerialDeviceController
import time, binascii
from utils.logger import log_error

class G2Controller(SerialDeviceController):
    def __init__(self):
        super().__init__(baudrate=9600, timeout=2, name="Time Machine G2")

    def initialize(self):
        # According to G2 protocol: send handshake sequence and check response
        for attempt in range(3):
            try:
                response = self.send_command(b'INIT\n')
                if b'READY' in response:
                    return True
            except Exception as e:
                log_error(f"[G2 INIT] Attempt {attempt}: {e}")
                time.sleep(2**attempt)  # exponential backoff
        raise RuntimeError("Failed to initialize G2 after 3 attempts.")

    def poll_status(self):
        try:
            resp = self.send_command(b'STATUS\n')
            # Parse actual status per vendor format
            if b'OK' in resp:
                return "OK"
            elif b'ERR' in resp:
                log_error(f"[G2 STATUS ERROR] Raw: {resp}")
                return f"Device error: {resp.decode(errors='ignore')}"
            else:
                return f"Unknown status: {resp}"
        except Exception as e:
            log_error(e)
            return "Polling failed."

    def start_race(self):
        try:
            resp = self.send_command(b'START\n')
            return resp.decode(errors='ignore')
        except Exception as e:
            log_error(f"[G2 START] {e}")
            return "Failed to start race."

    def stop_race(self):
        try:
            resp = self.send_command(b'STOP\n')
            return resp.decode(errors='ignore')
        except Exception as e:
            log_error(f"[G2 STOP] {e}")
            return "Failed to stop race."

    def get_results(self):
        try:
            raw = self.send_command(b'RESULTS\n')
            # Parse as per actual byte layout for times/places
            return raw.decode(errors='ignore')
        except Exception as e:
            log_error(f"[G2 GET RESULTS] {e}")
            return "Unable to read results."

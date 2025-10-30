from controllers.base_controller import SerialDeviceController
import time
from utils.logger import log_error

class ColoradoController(SerialDeviceController):
    def __init__(self):
        super().__init__(baudrate=9600, timeout=2, name="Colorado")

    def initialize(self):
        # Colorado Systems handshake, per official docs
        for attempt in range(3):
            try:
                response = self.send_command(b'COLORADO_INIT\r\n')
                if b'READY' in response:
                    return True
            except Exception as e:
                log_error(f"[Colorado INIT] Attempt {attempt}: {e}")
                time.sleep(2**attempt)
        raise RuntimeError("Failed to initialize Colorado after 3 attempts.")

    def poll_status(self):
        try:
            resp = self.send_command(b'STATUS\r\n')
            if b'OK' in resp:
                return "OK"
            elif b'ERR' in resp:
                log_error(f"[Colorado STATUS ERROR] Raw: {resp}")
                return f"Device error: {resp.decode(errors='ignore')}"
            else:
                return f"Unknown status: {resp}"
        except Exception as e:
            log_error(e)
            return "Polling failed."

    def start_race(self):
        try:
            resp = self.send_command(b'START\r\n')
            return resp.decode(errors='ignore')
        except Exception as e:
            log_error(f"[Colorado START] {e}")
            return "Failed to start race."

    def stop_race(self):
        try:
            resp = self.send_command(b'STOP\r\n')
            return resp.decode(errors='ignore')
        except Exception as e:
            log_error(f"[Colorado STOP] {e}")
            return "Failed to stop race."

    def get_results(self):
        try:
            raw = self.send_command(b'RESULTS\r\n')
            # Actual parsing code here...
            return raw.decode(errors='ignore')
        except Exception as e:
            log_error(f"[Colorado RESULTS] {e}")
            return "Unable to read results."

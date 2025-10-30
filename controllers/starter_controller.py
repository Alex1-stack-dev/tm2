from controllers.base_controller import SerialDeviceController
import time
from utils.logger import log_error

class StarterController(SerialDeviceController):
    def __init__(self):
        super().__init__(baudrate=9600, timeout=1, name="Starter System")

    def listen_for_start(self):
        # Listen for the start signal according to vendor protocol
        while True:
            try:
                with self.open_connection() as conn:
                    # Replace with real hardware byte/pin checks
                    if conn.in_waiting:
                        data = conn.readline()
                        if b'START' in data:
                            return True
                time.sleep(0.1)
            except Exception as e:
                log_error(f"[Starter LISTEN] {e}")
                time.sleep(1)

    def trigger_start(self):
        try:
            resp = self.send_command(b'TRIGGER\n')
            return resp.decode(errors='ignore')
        except Exception as e:
            log_error(f"[Starter TRIGGER] {e}")
            return "Unable to trigger start."

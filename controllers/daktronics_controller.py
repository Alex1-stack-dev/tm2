from controllers.base_controller import SerialDeviceController
import time
from utils.logger import log_error

class DaktronicsController(SerialDeviceController):
    def __init__(self):
        super().__init__(baudrate=19200, timeout=2, name="Daktronics")

    def initialize(self):
        for attempt in range(3):
            try:
                response = self.send_command(b'INIT\n')
                if b'READY' in response:
                    return True
            except Exception as e:
                log_error(f"[Daktronics INIT] Attempt {attempt}: {e}")
                time.sleep(2**attempt)
        raise RuntimeError("Failed to initialize Daktronics after 3 attempts.")

    def send_status(self, status:str):
        try:
            resp = self.send_command(status.encode('ascii'))
            return resp.decode(errors='ignore')
        except Exception as e:
            log_error(f"[Daktronics STATUS] {e}")
            return f"Error sending status: {e}"

    def get_times(self):
        try:
            data = self.send_command(b'GET_TIMES\n')
            # Actual parsing for Daktronics protocol
            return data.decode(errors='ignore')
        except Exception as e:
            log_error(f"[Daktronics TIMES] {e}")
            return "Unable to get times."

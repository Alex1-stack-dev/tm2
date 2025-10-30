import serial
from utils.logger import log_error
class DaktronicsController:
    def send_status(self, status):
        try:
            s = serial.Serial('/dev/ttyUSB2', 9600)
            s.write(status.encode('ascii'))
            s.close()
        except Exception as e:
            log_error(e)

import serial
from utils.logger import log_error
class ColoradoController:
    def __init__(self):
        self.port = "/dev/ttyUSB1"
    def start_race(self):
        try:
            s = serial.Serial(self.port, 9600, timeout=1)
            s.write(b'START\r\n')  # Implement correct protocol command
            response = s.readline()
            s.close()
            return response.decode()
        except Exception as e:
            log_error(e)
            return str(e)

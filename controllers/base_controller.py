import serial
from serial.tools import list_ports
import platform
import time
import threading
from utils.logger import log_error

class SerialDeviceController:
    def __init__(self, baudrate=9600, timeout=2, name="Device"):
        self.port = None
        self.baudrate = baudrate
        self.timeout = timeout
        self.name = name

    def list_ports(self):
        return list_ports.comports()

    def auto_select_port(self):
        ports = self.list_ports()
        if not ports:
            raise RuntimeError(f"No serial ports detected for {self.name}.")
        self.port = ports[0].device
        return self.port

    def open_connection(self):
        if not self.port:
            self.auto_select_port()
        try:
            connection = serial.Serial(
                self.port, self.baudrate, timeout=self.timeout
            )
            return connection
        except Exception as e:
            log_error(f"Cannot connect to {self.name}: {e}")
            raise

    def send_command(self, cmd_bytes, wait_response=True):
        with self.open_connection() as conn:
            conn.write(cmd_bytes)
            if wait_response:
                return conn.readline()
        return b''

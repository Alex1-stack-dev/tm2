import serial
import struct
import logging

class G2ProtocolError(Exception):
    pass

class G2Protocol:
    
    BAUDRATE = 19200
    BYTE_SIZE = 8
    PARITY = serial.PARITY_NONE
    STOPBITS = serial.STOPBITS_ONE
    TIMEOUT = 2

    @staticmethod
    def build_command(cmd: str) -> bytes:
        """
        Build a G2 protocol command string (ASCII with CR).
        """
        return (cmd + '\r').encode('ascii')

    @staticmethod
    def parse_response(resp: bytes) -> str:
        """
        Decode and clean up a response from the G2 device.
        """
        try:
            return resp.decode('ascii').strip('\r\n')
        except Exception as e:
            logging.error(f"Failed to decode G2 response: {e}")
            raise G2ProtocolError()

    @classmethod
    def default_serial_params(cls):
        return {
            'baudrate': cls.BAUDRATE,
            'bytesize': cls.BYTE_SIZE,
            'parity': cls.PARITY,
            'stopbits': cls.STOPBITS,
            'timeout': cls.TIMEOUT
        }

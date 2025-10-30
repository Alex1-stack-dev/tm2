import asyncio
import serial_asyncio
import logging
from .g2_protocol import G2Protocol, G2ProtocolError
from .timing_types import TimingEvent, Race, RaceResult
import datetime
from typing import List, Optional

class AsyncG2Controller:
    """
    Asynchronous G2 controller using asyncio and serial_asyncio.
    """
    def __init__(self, port: str):
        self.port = port
        self.transport = None
        self.protocol = None
        self.loop = asyncio.get_event_loop()

    async def connect(self):
        try:
            params = G2Protocol.default_serial_params()
            self.transport, self.protocol = await serial_asyncio.create_serial_connection(
                self.loop, lambda: G2AsyncProtocol(), self.port, **params)
            logging.info(f"Connected to G2 device on port {self.port}")
        except Exception as e:
            logging.error(f"Async serial connection error: {e}")
            raise

    async def send_command(self, command: str) -> str:
        try:
            await self.protocol.send_command(command)
            response = await self.protocol.read_response()
            return response
        except Exception as e:
            logging.error(f"G2 async command failed: {command}, {e}")
            raise

    async def start_race(self):
        resp = await self.send_command('START')
        logging.info(f"Started race (G2 response: {resp})")

    async def stop_race(self):
        resp = await self.send_command('STOP')
        logging.info(f"Stopped race (G2 response: {resp})")

    async def read_times(self) -> List[RaceResult]:
        resp = await self.send_command('READTIMES')
        results = []
        for line in resp.splitlines():
            try:
                part_id, finish_str = line.split(',')
                minsec = finish_str.split(':')
                minutes = int(minsec[0])
                seconds, hundredths = map(int, minsec[1].split('.'))
                td = datetime.timedelta(minutes=minutes, seconds=seconds, milliseconds=hundredths*10)
                results.append(RaceResult(participant_id=int(part_id), finish_time=td))
            except Exception as e:
                logging.warning(f"Failed to parse line '{line}': {e}")
        return results

    async def close(self):
        if self.transport:
            self.transport.close()
            logging.info("Closed async serial connection.")

class G2AsyncProtocol(asyncio.Protocol):
    def __init__(self):
        self.buffer = b''
        self.transport = None
        self.response_event = asyncio.Event()

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        self.buffer += data
        if b'\r\n' in self.buffer:
            self.response_event.set()

    async def send_command(self, cmd):
        message = G2Protocol.build_command(cmd)
        self.buffer = b''
        self.response_event.clear()
        self.transport.write(message)

    async def read_response(self):
        await self.response_event.wait()
        resp = G2Protocol.parse_response(self.buffer)
        self.buffer = b''
        return resp

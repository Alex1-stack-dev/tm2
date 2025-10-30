import asyncio, serial_asyncio
from utils.logger import log_error
class G2Controller:
    async def start_race_async(self):
        try:
            reader, writer = await serial_asyncio.open_serial_connection(url='/dev/ttyUSB0', baudrate=9600)
            writer.write(b'START\n')
            await writer.drain()
            data = await reader.readline()
            return data.decode()
        except Exception as e:
            log_error(e)
            return str(e)
    def start_race(self):
        return asyncio.run(self.start_race_async())

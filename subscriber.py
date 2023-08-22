import asyncio
import logging

from nats.aio.client import Client as NATS

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Subscriber:
    def __init__(self):
        self.loop = asyncio.new_event_loop()
    
    def run(self):
        self.loop.run_until_complete(self.subscribe())
        self.loop.run_forever()

    async def subscribe(self):
        logger.info(f"in NATS main")
        nc = NATS()

        async def message_handler(msg):
            logger.info(f"In nats handler")
            subject = msg.subject
            data = msg.data.decode()
            logger.info(f"Received a message on '{subject}': {data}")
        logging.info("Harsh natssssssss")
        await nc.connect("nats://nats:4222", loop=self.loop)  # Connect to NATS server
        sid = await nc.subscribe("test", cb=message_handler)  # Subscribe to subject
        logger.info(f"NATS connected")
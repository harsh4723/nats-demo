import asyncio
import logging

from nats.aio.client import Client as NATS

class Subscriber:
    def __init__(self):
        self.loop = asyncio.new_event_loop()
    
    def run(self):
        self.loop.run_until_complete(self.subscribe())
        self.loop.run_forever()

    async def subscribe(self):
        logging.info(f"in NATS main")
        nc = NATS()

        options = {"servers": "nats://nats:4222", "loop": self.loop, "dont_randomize": True}

        async def disconnected_cb():
            logging.warning("Got disconnected from nats!")

        async def reconnected_cb():
            # See who we are connected to on reconnect.
            logging.info("Got reconnected to {url}".format(url=nc.connected_url.netloc))

        async def error_cb(e):
            logging.warning("There was an error: {}".format(e))

        async def closed_cb():
            logging.info("NATS connection is closed")

        async def message_handler(msg):
            logging.info(f"In nats handler")
            subject = msg.subject
            data = msg.data.decode()
            logging.info(f"Received a message on '{subject}': {data}")
    
        options["disconnected_cb"] = disconnected_cb
        options["reconnected_cb"] = reconnected_cb
        options["max_reconnect_attempts"] = -1
        options["connect_timeout"] = 5  # 5 sec
        options["error_cb"] = error_cb
        options["closed_cb"] = closed_cb

    
        logging.info("Harsh natssssssss")
        try:
            await nc.connect(**options)
        except Exception as e:
            logging.error("Error occurred while connecting to nats server: {}".format(e))
        # await nc.connect("nats://nats:4222", loop=self.loop)  # Connect to NATS server
        await nc.subscribe("test", cb=message_handler)  # Subscribe to subject
        logging.info(f"NATS connected")
import asyncio
from nats.aio.client import Client as NATS
import logging

async def subscribe(loop):
    logging.info(f"in NATS main")
    print("Harsh NATS main")
    nc = NATS()

    options = {"servers": "nats-bridge-internal.prod.use-1d.infra:4222", "loop": loop, "dont_randomize": True}

    async def disconnected_cb():
        logging.warning("Got disconnected from nats!")
        print("Harsh disconnected")

    async def reconnected_cb():
        # See who we are connected to on reconnect.
        print("Harsh reconnected")
        logging.info("Got reconnected to {url}".format(url=nc.connected_url.netloc))

    async def error_cb(e):
        print("Harsh error")
        logging.warning("There was an error: {}".format(e))

    async def closed_cb():
        logging.info("NATS connection is closed")
        print("Nats closed")

    async def message_handler(msg):
        print("Handler invoked")
        logging.info(f"In nats handler")
        subject = msg.subject
        data = msg.data.decode()
        print(f"received message:{data}")
        logging.info(f"Received a message on '{subject}': {data}")

    options["disconnected_cb"] = disconnected_cb
    options["reconnected_cb"] = reconnected_cb
    options["max_reconnect_attempts"] = -1
    options["connect_timeout"] = 5  # 5 sec
    options["error_cb"] = error_cb
    options["closed_cb"] = closed_cb
    options["reconnect_time_wait"] = 1
    options["max_outstanding_pings"] = 20
    options["ping_interval"] = 30


    logging.info("Harsh natssssssss")
    print("Harsh natsssss")
    try:
        await nc.connect(**options)
    except Exception as e:
        logging.error("Error occurred while connecting to nats server: {}".format(e))
    # await nc.connect("nats://nats:4222", loop=self.loop)  # Connect to NATS server
    await nc.subscribe("testH", cb=message_handler)  # Subscribe to subject
    logging.info(f"NATS connected")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(subscribe(loop))
    loop.run_forever()

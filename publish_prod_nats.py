import asyncio
from nats.aio.client import Client as NATS

async def publish():
    nc = NATS()

    await nc.connect("nats-bridge-internal.prod.use-1d.infra:4222")
    message = "Hello, NATS!"
    try:
        await nc.publish("testH", message.encode())
        print(f"Published message: {message}")
    except Exception as e:
        print("Exception while publishing")
    finally:
        await nc.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(publish(loop))

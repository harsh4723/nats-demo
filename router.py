import asyncio
from nats.aio.client import Client as NATS
import logging
from fastapi import FastAPI, HTTPException, APIRouter
import uvicorn
from configservice import AlbusConfigManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

router = APIRouter()

# async def message_handler(msg):
#     logger.info(f"In nats handler")
#     subject = msg.subject
#     data = msg.data.decode()
#     logger.info(f"Received a message on '{subject}': {data}")

# async def main(loop):
#     logger.info(f"in NATS main")
#     nc = NATS()

#     await nc.connect("nats://nats:4222", loop=loop)  # Connect to NATS server
#     sid = await nc.subscribe("test", cb=message_handler)  # Subscribe to subject
#     logger.info(f"NATS connected")


@router.get("/hello/{message}")
async def sample_test(message: str):
    logger.info(f"Hellooooooooooooo")
    return {"status": "Hello from other side"}

def load_models():
    logging.info("harsh main of router")
    config_manager = AlbusConfigManager()
    config_manager.register_client()

if __name__ == "__main__":
    logger.info(f"before uvicorn")
    logging.info("harsh main of router")
    #uvicorn.run(app, host="0.0.0.0", port=8001)
    logger.info(f"after uvicorn")

    # config_manager = AlbusConfigManager()
    # config_manager.register_client()

    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main(loop))
    # loop.run_forever()

import asyncio
from nats.aio.client import Client as NATS
import logging
from fastapi import FastAPI, HTTPException, APIRouter
import uvicorn
from configservice import AlbusConfigManager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

router = APIRouter()

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

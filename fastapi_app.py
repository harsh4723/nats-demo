from fastapi import FastAPI, HTTPException
import asyncio
from nats.aio.client import Client as NATS

app = FastAPI()

@app.get("/publish/{subject}/{message}")
async def publish_to_nats(subject: str, message: str):
    nc = NATS()

    await nc.connect("nats://nats:4222")  # Service name from docker-compose.yml

    try:
        await nc.publish(subject, message.encode())
        return {"status": "Message published successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await nc.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

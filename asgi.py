from fastapi import FastAPI

from router import router as api_router, load_models

def get_application() -> FastAPI:
    app = FastAPI(title="Reranker!!")
    load_models()
    app.include_router(api_router)
    return app

asgi = get_application()

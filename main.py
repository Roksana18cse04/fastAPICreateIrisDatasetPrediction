from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.endpoints.iris import router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Iris Species Prediction API",
    version="1.0.0"
)

app.include_router(router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
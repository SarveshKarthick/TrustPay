from fastapi import FastAPI
from app.config.settings import settings
from app.users.router import router as users_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(users_router)


@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} Running 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

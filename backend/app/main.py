from fastapi import FastAPI

app = FastAPI(
    title="TrustPay API",
    description="Backend API for TrustPay",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "TrustPay Backend Running 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

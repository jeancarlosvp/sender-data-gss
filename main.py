from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
from app.config import CORS_ORIGINS
from app.datapayments.routers import router as datapayments_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(datapayments_router)

@app.get("/")
def root() -> Dict[str, object]:
    return {"message": "Bienvenido al servicio de DataPayments writer"}
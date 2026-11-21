from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine
from notificacoes.rotas import router as notificacoes_router
from notificacoes.consumidor import iniciar_consumidor
import logging

logging.basicConfig(level=logging.INFO)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Microsserviço de Notificações")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notificacoes_router)

@app.on_event("startup")
def startup():
    iniciar_consumidor()

@app.get("/saude")
def health_check():
    return {"status": "ok", "servico": "notificacoes"}
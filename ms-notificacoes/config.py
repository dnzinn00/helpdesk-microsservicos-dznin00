import logging
import os
import secrets

log = logging.getLogger("helpdesk")

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:senha123@localhost:5436/notificacoes_db")
REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

JWT_SEGREDO = os.getenv("JWT_SEGREDO", "super_segredo_usuarios")
if not JWT_SEGREDO:
    log.warning("JWT_SEGREDO não definido; usando um segredo aleatório.")
    JWT_SEGREDO = secrets.token_urlsafe(48)

JWT_ALGORITMO = "HS256"
JWT_EMISSOR = "helpdesk-ti"
TOKEN_MINUTOS = int(os.getenv("TOKEN_MINUTOS", "60"))
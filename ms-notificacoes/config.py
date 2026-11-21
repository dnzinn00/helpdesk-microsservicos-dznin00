import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:senha123@localhost:5436/notificacoes_db")
REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
JWT_SEGREDO = os.getenv("JWT_SEGREDO", "super_segredo_usuarios")
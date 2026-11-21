import json
import threading
import redis
import logging
from database import SessionLocal
from notificacoes.modelos import Notificacao
from config import REDIS_URL

logger = logging.getLogger("ms-notificacoes")

def ouvir_eventos():
    """Loop infinito que escuta a fila de eventos do Redis."""
    logger.info("🎧 Consumidor de eventos iniciado. Escutando o canal 'canal_chamados'...")
    r = redis.from_url(REDIS_URL)
    pubsub = r.pubsub()
    pubsub.subscribe("canal_chamados")
    
    for mensagem in pubsub.listen():
        if mensagem["type"] != "message":
            continue
        try:
            evento = json.loads(mensagem["data"])
            tipo = evento.get("tipo")
            usuario_id = evento.get("usuario_id")
            texto = evento.get("mensagem")
            
            db = SessionLocal()
            try:
                notif = Notificacao(
                    usuario_id=usuario_id,
                    tipo=tipo,
                    mensagem=texto
                )
                db.add(notif)
                db.commit()
                logger.info(f"✅ Evento processado: {tipo} para usuário {usuario_id}")
            finally:
                db.close()
        except Exception as e:
            logger.error(f"❌ Erro ao processar evento: {e}")

def iniciar_consumidor():
    """Inicia o consumidor em uma thread separada."""
    thread = threading.Thread(target=ouvir_eventos, daemon=True)
    thread.start()
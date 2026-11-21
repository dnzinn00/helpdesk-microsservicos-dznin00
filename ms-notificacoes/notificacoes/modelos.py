from datetime import datetime
from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class Notificacao(Base):
    __tablename__ = "notificacoes"

    id: Mapped[int] = mapped_column(primary_key=True)
    usuario_id: Mapped[int] = mapped_column(Integer)
    tipo: Mapped[str] = mapped_column(String(50))
    mensagem: Mapped[str] = mapped_column(Text)
    criada_em: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
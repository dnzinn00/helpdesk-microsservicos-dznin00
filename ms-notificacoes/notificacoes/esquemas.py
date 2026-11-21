from datetime import datetime
from pydantic import BaseModel, ConfigDict

class NotificacaoSaida(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    usuario_id: int
    tipo: str
    mensagem: str
    criada_em: datetime
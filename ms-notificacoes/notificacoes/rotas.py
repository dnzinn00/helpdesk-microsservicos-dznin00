from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from database import get_db
from notificacoes.modelos import Notificacao
from notificacoes.esquemas import NotificacaoSaida

router = APIRouter(prefix="/notificacoes", tags=["Notificações"])

@router.get("", response_model=list[NotificacaoSaida])
def listar_notificacoes(db: Session = Depends(get_db)):
    # Por enquanto, lista todas (o ideal seria filtrar pelo usuário do token)
    return list(db.scalars(select(Notificacao).order_by(Notificacao.id.desc())))
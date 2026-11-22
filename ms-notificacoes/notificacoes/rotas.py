from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from database import get_db
from notificacoes.modelos import Notificacao
from notificacoes.esquemas import NotificacaoSaida
from auth.dependencias import usuario_atual, UsuarioToken

router = APIRouter(prefix="/notificacoes", tags=["Notificações"])

@router.get("", response_model=list[NotificacaoSaida])
def listar_notificacoes(usuario: UsuarioToken = Depends(usuario_atual), db: Session = Depends(get_db)):
    print(f"🔍 Buscando notificações para o usuário ID: {usuario.id} ({usuario.perfil})")
    resultado = list(db.scalars(
        select(Notificacao)
        .where(Notificacao.usuario_id == usuario.id)
        .order_by(Notificacao.id.desc())
    ))
    print(f"📋 Encontradas {len(resultado)} notificações")
    return resultado
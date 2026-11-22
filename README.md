# HelpDesk TI · Microsserviços

Este projeto é a evolução do sistema HelpDesk TI monolítico para uma **arquitetura de microsserviços**, conforme solicitado na disciplina de Arquitetura de Software.

## 📐 Arquitetura

O sistema foi dividido em **três microsserviços independentes**, cada um com seu próprio banco de dados PostgreSQL, além de um **API Gateway** como ponto único de entrada.

```mermaid
graph TD
    Tela[Tela do HelpDesk] --> Gateway[API Gateway<br>Porta 8000]

    Gateway --> MS_Usuarios[MS Usuários<br>Porta 8001]
    Gateway --> MS_Inventario[MS Inventário<br>Porta 8002]
    Gateway --> MS_Chamados[MS Chamados<br>Porta 8003]

    MS_Usuarios --> DB_Usuarios[(DB Usuários)]
    MS_Inventario --> DB_Inventario[(DB Inventário)]
    MS_Chamados --> DB_Chamados[(DB Chamados)]

    MS_Chamados -.->|HTTP /usuarios/{id}| MS_Usuarios
    MS_Chamados -.->|HTTP /ativos/{id}| MS_Inventario

### Serviços

Serviço                 | Porta |      Responsabilidade |                                     Banco de Dados
| ------------------ | :--------: | :-----------------------------------------------------: | :-----------:  |
| API Gateway        |   8000  |   Ponto único de entrada, roteamento e entrega do frontend  |      -        |
| MS Usuários        |   8001  |   Autenticação (JWT), usuários e perfis                     | usuarios_db   |
| MS Inventário      |   8002  |   Equipamentos de TI                                        | inventario_db |
| MS Chamados        |   8003  |   Abertura, atribuição, status e comentários                | chamados_db   |
```

Decisões de Arquitetura

1. Banco de dados por serviço: Cada microsserviço tem seu próprio banco PostgreSQL, eliminando o acoplamento de dados do monólito.

2. Comunicação síncrona (HTTP): O ms-chamados consulta o ms-usuarios e o ms-inventario via HTTP (com timeout e tratamento de falhas) para validar dados.

3. Autenticação compartilhada: O token JWT gerado pelo ms-usuarios é validado por todos os serviços usando o mesmo JWT_SEGREDO. As permissões por perfil são mantidas.

4. API Gateway: Centraliza o acesso, serve o frontend e redireciona as chamadas para os serviços corretos, mantendo a tela funcionando sem alterações.

5. Docker Compose: Orquestra todos os serviços, bancos e o Gateway com um único comando.

🚀 COMO RODAR
PRÉ-REQUISITOS:
Docker e Docker Compose instalados

Subir tudo
docker compose up -d --build

Acessar a aplicação
• Tela do HelpDesk: http://localhost:8000/

• Documentação do Gateway: http://localhost:8000/docs

• Saúde dos serviços: http://localhost:8000/saude

Contas de exemplo
E-mail Perfil Senha
admin@empresa.com | Administrador | Helpdesk2026
carla@empresa.com | Técnica | Helpdesk2026
diego@empresa.com | Técnico | Helpdesk2026
ana@empresa.com | Solicitante | Helpdesk2026
bruno@empresa.com | Solicitante | Helpdesk2026

🧪 Testes
O projeto mantém os testes de segurança originais adaptados para cada serviço:
pytest -q

## 📹 Vídeo de Demonstração

https://youtu.be/cQ0H3Vqeu4g

O vídeo mostra a arquitetura, o fluxo completo de um chamado, a segurança entre serviços e a falha de um serviço (simulando a queda do Inventário).

# Telegram Bot

Este é um bot do Telegram que gerencia regras de encaminhamento de mensagens entre canais. O bot também suporta pagamentos via Stripe.

## Configuração

1. Clone o repositório:
   ```bash
   git clone https://github.com/Kronos1027/telegram_bot.git
   cd telegram_bot
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente. Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:
   ```env
   TELEGRAM_TOKEN=seu_token_do_telegram
   STRIPE_API_KEY=sua_chave_api_stripe
   STRIPE_WEBHOOK_SECRET=sua_chave_webhook_stripe
   STRIPE_MONTHLY_PRICE_ID=preco_mensal_id
   STRIPE_ANNUAL_PRICE_ID=preco_anual_id
   DB_NAME=nome_do_banco
   DB_USER=usuario_do_banco
   DB_PASSWORD=senha_do_banco
   DB_HOST=host_do_banco
   ```

5. Inicialize o banco de dados:
   ```bash
   python init_db.py
   ```

6. Execute o bot:
   ```bash
   python bot.py
   ```

## Estrutura do Projeto

- `bot.py`: Arquivo principal do bot.
- `init_db.py`: Script para inicializar o banco de dados.
- `handlers/`: Diretório contendo os handlers do bot.
- `translations/`: Diretório contendo as traduções.
- `utils/`: Diretório contendo funções utilitárias.

import os
import psycopg2
from psycopg2.extras import DictCursor

def get_db_connection():
    return psycopg2.connect(
        dbname=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        host=os.environ.get("DB_HOST")
    )

def init_db():
    conn = get_db_connection()
    with conn.cursor() as cur:
        # Tabela de usuários
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id BIGINT PRIMARY KEY,
                username TEXT,
                language TEXT DEFAULT 'pt',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabela de regras
        cur.execute('''
            CREATE TABLE IF NOT EXISTS rules (
                rule_id SERIAL PRIMARY KEY,
                user_id BIGINT REFERENCES users(user_id),
                name TEXT,
                source_channel_id BIGINT,
                destination_channel_id BIGINT,
                active BOOLEAN DEFAULT TRUE,
                filter_text TEXT,
                replace_links BOOLEAN DEFAULT FALSE,
                replacement_text TEXT,
                add_prefix TEXT,
                add_suffix TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_payment TIMESTAMP,
                subscription_id TEXT
            )
        ''')
        
        # Tabela de mensagens encaminhadas
        cur.execute('''
            CREATE TABLE IF NOT EXISTS forwarded_messages (
                id SERIAL PRIMARY KEY,
                rule_id INTEGER REFERENCES rules(rule_id),
                source_message_id BIGINT,
                destination_message_id BIGINT,
                source_channel_id BIGINT,
                destination_channel_id BIGINT,
                forwarded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabela de logs
        cur.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id SERIAL PRIMARY KEY,
                user_id BIGINT REFERENCES users(user_id),
                rule_id INTEGER REFERENCES rules(rule_id),
                log_channel_id BIGINT,
                message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Tabela de pagamentos
        cur.execute('''
            CREATE TABLE IF NOT EXISTS payments (
                id SERIAL PRIMARY KEY,
                user_id BIGINT REFERENCES users(user_id),
                rule_id INTEGER REFERENCES rules(rule_id),
                amount DECIMAL(10, 2),
                currency TEXT DEFAULT 'BRL',
                payment_method TEXT,
                status TEXT,
                stripe_payment_id TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
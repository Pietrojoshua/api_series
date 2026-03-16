from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from os import getenv
from dotenv import load_dotenv

load_dotenv()  # Carrega o .env

# URLs de conexão usando variáveis de ambiente
DB_USER = getenv("DB_USER")
DB_PSWD = getenv("DB_PSWD")
DB_HOST = getenv("DB_HOST")
DB_NAME = getenv("DB_NAME")

SERVER_URL = f"mysql+pymysql://{DB_USER}:{DB_PSWD}@{DB_HOST}"
DATABASE_URL = f"{SERVER_URL}/{DB_NAME}"

# Criação do banco, se não existir
engine_server = create_engine(SERVER_URL)
with engine_server.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
    conn.commit()

# Conexão com o banco já criado
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Injeção de dependência para rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
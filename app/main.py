from fastapi import FastAPI
from app.database import Base, engine
from app.route.serie import serie

# Cria todas as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclui o router
app.include_router(serie)

@app.get("/")
async def health_check():
    return {"status": "API Online"}
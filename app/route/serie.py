from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.model.serie import SerieModel
from app.schema.serie import SerieSchema

serie = APIRouter()

@serie.post("/")
async def criar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(**dados.model_dump())
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie

@serie.get("/series")
async def listar_series(db: Session = Depends(get_db)):
    return db.query(SerieModel).all()

@serie.put("/{serie_id}")
async def atualizar_serie(serie_id: int, dados: SerieSchema, db: Session = Depends(get_db)):
    serie_db = db.query(SerieModel).filter(SerieModel.id == serie_id).first()
    if not serie_db:
        raise HTTPException(status_code=404, detail="Série não encontrada")
    for key, value in dados.model_dump().items():
        setattr(serie_db, key, value)
    db.commit()
    db.refresh(serie_db)
    return serie_db

@serie.delete("/{serie_id}")
async def deletar_serie(serie_id: int, db: Session = Depends(get_db)):
    serie_db = db.query(SerieModel).filter(SerieModel.id == serie_id).first()
    if not serie_db:
        raise HTTPException(status_code=404, detail="Série não encontrada")
    db.delete(serie_db)
    db.commit()
    return {"detail": "Série deletada com sucesso"}
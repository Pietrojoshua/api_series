from pydantic import BaseModel
from typing import Optional

class SerieSchema(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    ano_lancamento: int

    class Config:
        from_attributes = True  # Pydantic v2
        # Para Pydantic v1: use orm_mode = True
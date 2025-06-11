import os
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Configuration DB depuis les variables d’environnement
DB_USER = os.getenv("POSTGRES_USER", "fastapi_user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "supersecret")
DB_NAME = os.getenv("POSTGRES_DB", "fastapi_db")
DB_HOST = os.getenv("POSTGRES_HOST", "db")  # 'db' = nom du service dans docker-compose

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}"

# Initialisation SQLAlchemy
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# Modèle DB
class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)

# Création des tables
Base.metadata.create_all(bind=engine)

# Modèle Pydantic
class ItemCreate(BaseModel):
    name: str
    description: str = None

app = FastAPI()

# Dépendance pour la session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET /health
@app.get("/health")
def health_check():
    return {"status": "API is up and running"}

# POST /items/
@app.post("/items/")
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return {"message": "Item created", "item": db_item}

# GET /items/{item_id}
@app.get("/items/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

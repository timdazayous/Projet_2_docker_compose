import os
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager

from app_api.models.models import DataItem
from app_api.modules import crud, connect
from app_api.maths import mon_module

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Création des tables dans la base par défaut
    connect.Base.metadata.create_all(bind=connect.engine)
    
    # Logique de démarrage optionnelle (ex: lire le CSV)
    csv_path = os.path.join(os.path.dirname(__file__), "data", "moncsv.csv")
    print("Démarrage de l'API...")
    mon_module.print_data(csv_path)
    yield
    print("Arrêt de l'API...")

app = FastAPI(title="Projet 2 API", lifespan=lifespan)

@app.post("/data", response_model=DataItem, status_code=201)
def create_data(item: DataItem, db: Session = Depends(connect.get_db)):
    """Sauvegarde une nouvelle donnée dans la BDD."""
    crud.create_record(db=db, item=item)
    return item

@app.get("/data")
def read_data(skip: int = 0, limit: int = 100, db: Session = Depends(connect.get_db)):
    """Récupère les données depuis la BDD."""
    records = crud.get_all_records(db, skip=skip, limit=limit)
    return records

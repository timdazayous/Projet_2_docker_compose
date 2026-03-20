import os
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager

from app_api.models.models import DataItem, MathRequest, SquareRequest
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

# Servir la documentation Sphinx (Statique)
# On utilise /docs/static pour ne pas entrer en conflit avec /docs (Swagger)
docs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs", "build", "html"))
if os.path.exists(docs_path):
    app.mount("/docs/static", StaticFiles(directory=docs_path), name="static_docs")

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

@app.post("/math/add")
def math_add(request: MathRequest):
    """Effectue une addition via le module maths."""
    result = mon_module.add(request.a, request.b)
    return {"a": request.a, "b": request.b, "operation": "addition", "result": result}

@app.post("/math/sub")
def math_sub(request: MathRequest):
    """Effectue une soustraction via le module maths."""
    result = mon_module.sub(request.a, request.b)
    return {"a": request.a, "b": request.b, "operation": "soustraction", "result": result}

@app.post("/math/square")
def math_square(request: SquareRequest):
    """Effectue un calcul de carré via le module maths."""
    result = mon_module.square(request.a)
    return {"a": request.a, "operation": "carre", "result": result}

from pydantic import BaseModel

class DataItem(BaseModel):
    """Modèle de données pour valider les entrées de l'API FastAPI."""
    nom: str
    age: int
    ville: str

class MathRequest(BaseModel):
    """Requête pour les opérations binaires (add, sub)."""
    a: float
    b: float

class SquareRequest(BaseModel):
    """Requête pour le carré d'un nombre."""
    a: float

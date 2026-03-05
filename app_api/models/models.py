from pydantic import BaseModel

class DataItem(BaseModel):
    """Modèle de données pour valider les entrées de l'API FastAPI."""
    nom: str
    age: int
    ville: str

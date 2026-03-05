from sqlalchemy.orm import Session
from app_api.models.models import DataItem
from app_api.modules.connect import DataRecord

def create_record(db: Session, item: DataItem):
    """Crée un nouvel enregistrement dans la base de données."""
    db_record = DataRecord(nom=item.nom, age=item.age, ville=item.ville)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def get_all_records(db: Session, skip: int = 0, limit: int = 100):
    """Récupère tous les enregistrements de la base de données."""
    return db.query(DataRecord).offset(skip).limit(limit).all()

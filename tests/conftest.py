import pytest
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app_api.main import app
from app_api.modules.connect import Base, get_db, DataRecord  # noqa: F401

# Configuration d'une base de données SQLite en mémoire pour les tests
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="session", autouse=True)
def setup_db():
    # Crée toutes les tables dans la BDD SQLite en mémoire
    Base.metadata.create_all(bind=engine)
    yield
    # Nettoie après les tests
    Base.metadata.drop_all(bind=engine)

@pytest.fixture
def db_session(setup_db):
    """Crée une nouvelle session de base de données pour chaque test."""
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture
def client(db_session):
    """
    Surcharge la dépendance get_db dans l'application FastAPI
    pour utiliser notre base de données de test en mémoire.
    """
    def override_get_db():
        try:
            yield db_session
        finally:
            pass
            
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    del app.dependency_overrides[get_db]

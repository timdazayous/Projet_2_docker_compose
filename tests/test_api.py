from fastapi.testclient import TestClient

def test_api_read_empty(client: TestClient):
    """Test initial quand la BDD est vide."""
    response = client.get("/data")
    assert response.status_code == 200
    assert response.json() == []

def test_api_create_data(client: TestClient):
    """Test de la route POST pour ajouter des données."""
    payload = {
        "nom": "Test User",
        "age": 25,
        "ville": "Paris"
    }
    response = client.post("/data", json=payload)
    assert response.status_code == 201
    
    data = response.json()
    assert data["nom"] == "Test User"
    assert data["age"] == 25
    assert data["ville"] == "Paris"

def test_api_read_after_create(client: TestClient):
    """Test de la route GET après ajout de données."""
    # On insère d'abord
    payload = {"nom": "Alice", "age": 30, "ville": "Lyon"}
    client.post("/data", json=payload)
    
    # On vérifie la lecture
    response = client.get("/data")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) > 0
    # Vérifie que Alice est bien dans la réponse
    assert any(item["nom"] == "Alice" for item in data)

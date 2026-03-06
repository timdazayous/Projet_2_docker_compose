from app_api.maths.mon_module import add, sub, square, print_data
import os

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0.5, 0.5) == 1.0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(10, 20) == -10
    assert sub(3.5, 1.5) == 2.0

def test_square():
    assert square(4) == 16
    assert square(-3) == 9
    assert square(0) == 0

def test_print_data(capsys):
    """Test que la fonction lit bien le CSV sans crasher et affiche quelque chose."""
    # On crée un petit fichier CSV temporaire pour le test
    test_csv_path = "test_data.csv"
    with open(test_csv_path, "w", encoding="utf-8") as f:
        f.write("nom,age,ville\nTestName,99,TestCity\n")
    
    try:
        print_data(test_csv_path)
        # Capture la sortie standard
        captured = capsys.readouterr()
        
        # Vérifie que la sortie contient les données du CSV
        assert "TestName" in captured.out
        assert "99" in captured.out
        assert "TestCity" in captured.out
    finally:
        # Nettoyage
        if os.path.exists(test_csv_path):
            os.remove(test_csv_path)

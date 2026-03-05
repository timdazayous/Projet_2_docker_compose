def add(a: float, b: float) -> float:
    """Additionne deux nombres."""
    return a + b

def sub(a: float, b: float) -> float:
    """Soustrait le second nombre au premier."""
    return a - b

def square(a: float) -> float:
    """Retourne le carré du nombre."""
    return a * a

def print_data(filepath: str) -> None:
    """Lit un fichier CSV et affiche son contenu dans la console."""
    import csv
    try:
        with open(filepath, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {filepath} est introuvable.")

import requests
from config import HEADERS


def validate_number(number_7char: str) -> bool:
    return len(number_7char) == 7 and number_7char.isdigit()


def build_case_id(prefix: str, number_7char: str, year: int) -> str:
    if not validate_number(number_7char):
        raise ValueError("Le numéro doit contenir exactement 7 chiffres.")
    return f"{prefix}-{number_7char}-{year}"


def fetch_case(case_id: str) -> bool:
    url = f"https://services.pacourts.us/public/v1/cases/{case_id}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=3, verify=False)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Erreur réseau pour {case_id} : {e}")
        return False


def check_case(prefix: str, number_7char: str, start_year: int = 2018) -> bool:
    """
    Vérifie si le case_id existe en validant le numéro et en appelant l'API.
    On incrémente le numéro et passe à l'année suivante après 50 échecs.
    """
    if not validate_number(number_7char):
        print("Numéro invalide. Il doit être composé de 7 chiffres.")
        return

    year = start_year
    num_attempts = 0

    if year > 2024:
        print("Année 2024 atteinte.")
        return

    # Boucle pour incrémenter les numéros jusqu'à 50
    while num_attempts < 50:
        case_id = build_case_id(prefix, number_7char, year)
        if fetch_case(case_id):
            print(f"Le case ID {case_id} existe.")
            return True
        else:
            print(f"Le case ID {case_id} n'existe pas.")
            num_attempts += 1
            # Incrémenter le numéro à chaque échec
            number_7char = str(int(number_7char) + 1).zfill(7)

    # Si 50 tentatives échouent, passer à l'année suivante
    year += 1
    print(f"Passage à l'année suivante: {year}")

    # Recommencer à partir de l'année suivante avec le même numéro de départ
    return check_case(prefix, number_7char, year)


prefix = "MJ-02000-CR"
number_7char = "000001"
start_year = 2018

check_case(prefix, number_7char)

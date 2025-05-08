import requests
from config import HEADERS


def validate_number(number_7char: str) -> bool:
    return len(number_7char) == 7 and number_7char.isdigit()


def fetch_case(case_id: str) -> bool:
    url = f"https://services.pacourts.us/public/v1/cases/{case_id}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=3, verify=False)
        return response.status_code == 200
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Erreur réseau pour {case_id} : {e}")
        return False


def check_cases(prefix: str, number_str: str, year_start: int=2018, max_attempts: int=50, max_years: int=7):
    if not validate_number(number_str):
        print("Numéro invalide. Il doit être composé de 7 chiffres.")
        return

    number = int(number_str)
    year = year_start
    attempt = 0
    failures = 0

    while year < year + max_years:
        while attempt < max_attempts:
            case_id = {prefix}-{number}-{year}
            if fetch_case(case_id):
                print(f"✅ Succès pour {case_id}")
            else:
                print(f"❌ Échec pour {case_id}")
                failures += 1
            number += 1

import requests
from config import YEARS, ID_PREFIX, MAX_FAILURES, BASE_URL, HEADERS
from utils import build_case_id, validate_case_id

def fetch_case(case_id: str) -> bool:
    url = f"{BASE_URL}/{case_id}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=3, verify=False)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"⚠️ Erreur réseau pour {case_id} : {e}")
        return False

def run_scraper():
    print("🚀 Démarrage du scraping...\n")

    for year in YEARS:
        print(f"🔎 Année : {year}")
        case_number = 1220
        consecutive_failures = 0
        while consecutive_failures < MAX_FAILURES:
            case_id = build_case_id(ID_PREFIX, case_number, year)
            print(f"🔍 Test : {case_id}")
            if fetch_case(case_id):
                print(f"✅ Succès pour {case_id}")
                consecutive_failures = 0
            else:
                print(f"❌ Échec pour {case_id}")
                consecutive_failures += 1
            case_number += 1
        print(f"⏭️  Passage à l'année suivante après {MAX_FAILURES} échecs.\n")

if __name__ == "__main__":
    run_scraper()

from config import YEARS, ID_PREFIX, MAX_FAILURES
from utils import build_case_id

def simulate_scraping():
    print("Début de la simulation du scraping...\n")

    for year in YEARS:
        print(f"🔎 Année : {year}")
        case_number = 1
        consecutive_failures = 0

        while consecutive_failures < MAX_FAILURES:
            case_id = build_case_id(ID_PREFIX, case_number, year)
            # --- Simulation : disons qu'on a une réponse quand le case_number est 8, 41, etc.
            has_response = case_number in {10, 50}  # à remplacer plus tard par un appel API
            if has_response:
                print(f"✅ Réponse trouvée pour {case_id}")
                consecutive_failures = 0  # reset si réponse
            else:
                print(f"❌ Aucune réponse pour {case_id}")
                consecutive_failures += 1
            case_number += 1

        print(f"⏭️  Passage à l'année suivante après {MAX_FAILURES} échecs consécutifs.\n")


if __name__ == "__main__":
    simulate_scraping()

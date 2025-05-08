BASE_URL = "https://services.pacourts.us/public/v1/cases"

HEADERS = {
    "Accept": "application/json",
    "Content-type": "application/json",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; Pixel Build/RQ1A.210105.003)",
    "Host": "services.pacourts.us",
    "Connection": "keep-alive",
    # 'Accept-Encoding': 'gzip, deflate, br',
}

YEARS = list(range(2018, 2025))

ID_PREFIX = "MJ-02000-CR"

MAX_FAILURES = 50

def format_case_number(number: int) -> str:
    return f"{number:07d}"

def build_case_id(base_id: str, number: int, year: int) -> str:
    formatted_number = format_case_number(number)
    return f"{base_id}-{formatted_number}-{year}"

def validate_case_id(prefix: str, number_7char: str, year: int) -> str:
    if len(number_7char) != 7 or not number_7char.isdigit():
        raise ValueError("Le numéro doit contenir exactement 7 chiffres.")
    return f"{prefix}-{number_7char}-{year}"
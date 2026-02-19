import re
from typing import List

def check_password(pwd: str) -> tuple[bool, str]:
    errors: List[str] = []
    if not pwd or len(pwd) < 8:
        errors.append("At least 8 characters")
    if not re.search(r"[a-z]", pwd):
        errors.append("Include a lowercase letter")
    if not re.search(r"[A-Z]", pwd):
        errors.append("Include an uppercase letter")
    if not re.search(r"\d", pwd):
        errors.append("Include a digit")
    if not re.search(r"[^\w\s]", pwd):
        errors.append("Include a symbol")
    if errors:
        return False, ", ".join(errors)
    return True, "Strong password"
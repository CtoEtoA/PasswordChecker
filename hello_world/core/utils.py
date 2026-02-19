import re
from typing import List

def check_password(password: str) -> tuple[bool, str]:
    errors: List[str] = []
    # Basic checks for demonstration purposes
    if not password or len(password) < 8:
        errors.append("At least 8 characters")
    if not re.search(r"[a-z]", password):
        errors.append("Include a lowercase letter")
    if not re.search(r"[A-Z]", password):
        errors.append("Include an uppercase letter")
    if not re.search(r"\d", password):
        errors.append("Include a digit")
    if not re.search(r"[^\w\s]", password):
        errors.append("Include a symbol")
    if errors:
        return False, ", ".join(errors)
    return True, "Strong Password"
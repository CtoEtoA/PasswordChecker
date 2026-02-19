import re
from typing import List, Tuple


def check_password(password: str) -> tuple[bool, str]:
    """Return (ok, message). On failure return a single prioritized error.

    The returned failure message is prefixed with "Password must have:" and
    uses the check with the highest priority (lowest int).
    """
    checks: List[Tuple[int, str]] = []
    pw = password or ""
    
    # Basic Checks
    # Priority numbers: lower = higher priority
    if len(pw) < 8:
        checks.append((1, "At least 8 characters"))
    if not re.search(r"[a-z]", pw):
        checks.append((5, "At least one lowercase letter"))
    if not re.search(r"[A-Z]", pw):
        checks.append((6, "At least one uppercase letter"))
    if not re.search(r"\d", pw):
        checks.append((4, "At least one digit"))
    if not re.search(r"[^\w\s]", pw):
        checks.append((3, "At least one symbol"))

    # More Special Checks
    if re.search(r'(.)\1+', pw.lower()):
        checks.append((2, "No repeated characters"))

    if checks:
        checks.sort(key=lambda t: t[0])
        _, msg = checks[0]
        return False, f"Password must have: {msg}"

    return True, "Strong Password"
import re
from typing import List, Tuple


def check_password(password: str) -> tuple[bool, str]:
    """Return (ok, message). On failure return a single prioritized error.

    The returned failure message is prefixed with "Password must have:" and
    uses the check with the highest priority (lowest int).
    """
    checks: List[Tuple[int, str]] = []
    password = password or ""
    
    # Basic Checks
    # Priority numbers: lower = higher priority
    if len(password) < 8:
        checks.append((1, "At least 8 characters"))
    if len(password) >128:
        checks.append((10, "Less than 128 characters"))
    if not re.search(r"[a-z]", password):
        checks.append((5, "At least one lowercase letter"))
    if not re.search(r"[A-Z]", password):
        checks.append((6, "At least one uppercase letter"))
    if not re.search(r"\d", password):
        checks.append((4, "At least one digit"))
    if not re.search(r"[^\w\s]", password):
        checks.append((3, "At least one symbol"))

    # More Special Checks
    if re.search(r"(.)\1+", password.lower()):
        checks.append((2, "No repeated characters"))
    if has_sequential(password):
        checks.append((7, "No sequential characters"))
    if password.strip() != password:
        checks.append((8, "No leading or trailing whitespace"))
    if re.search(r"\s{2,}", password):
        checks.append((9, "No consecutive whitespace"))
    if re.search(r"\d{1,2}[-/\.]\d{1,2}[-/\.]\d{2,4}|\d{4}[-/\.]\d{1,2}[-/\.]\d{1,2}|\b\d{4}\b", password):
        checks.append((11, "No dates"))
    if re.search(r"\d{4}", password):
        checks.append((12, "No 4-digit numbers"))
    
    if checks:
        checks.sort(key=lambda t: t[0])
        _, msg = checks[0]
        return False, f"Password must have: {msg}"

    return True, "Strong Password"

def has_sequential(s : str, n : int = 3):
    # Check for sequences of n or more characters (e.g. abc, 123, etc.)
    s = s.lower()
    for i in range(len(s)-n+1):
        seq = s[i:i+n]
        if all(ord(seq[j+1])-ord(seq[j])==1 for j in range(n-1)):
            return True
    return False
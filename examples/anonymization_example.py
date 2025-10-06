"""Anonymization and PII cleanup utilities."""
import hashlib
from typing import Optional

def hash_value(value: Optional[str]) -> Optional[str]:
    """Hash a string using SHA-256 and truncate for readability."""
    if not value:
        return value
    return hashlib.sha256(value.encode()).hexdigest()[:12]

def anonymize_attendee(row: dict) -> dict:
    """Return a copy of a record with PII fields anonymized."""
    r = dict(row)
    if r.get("email"):
        r["email"] = hash_value(r["email"])
    if r.get("userId"):
        r["userId"] = hash_value(str(r["userId"]))
    return r

if __name__ == "__main__":
    example = {"email": "user@example.com", "userId": "12345", "status": "approved"}
    print(anonymize_attendee(example))

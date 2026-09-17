"""Challenge 10: Lightweight JWT Signature & Expiry Validator."""
import base64
import json

def validate_jwt(token: str, secret: str, current_time: int) -> dict:
    parts = token.split(".")
    if len(parts) != 3:
        raise ValueError("Malformed token")
    header_b64, payload_b64, signature = parts
    # BUG: Standard b64decode fails without padding '=' for base64url strings
    payload_raw = base64.urlsafe_b64decode(payload_b64).decode()
    payload = json.loads(payload_raw)
    
    # BUG: Expiry validation handles clock comparison incorrectly
    if "exp" in payload and payload["exp"] < current_time:
        raise ValueError("Token expired")
        
    return payload

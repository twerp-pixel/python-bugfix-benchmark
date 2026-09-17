"""Reference Solution: Lightweight JWT Signature & Expiry Validator."""
import base64
import json
import hmac
import hashlib

def _pad_base64(s: str) -> str:
    remainder = len(s) % 4
    if remainder:
        s += "=" * (4 - remainder)
    return s

def validate_jwt(token: str, secret: str, current_time: int) -> dict:
    parts = token.split(".")
    if len(parts) != 3:
        raise ValueError("Malformed token")
    header_b64, payload_b64, signature_b64 = parts

    signing_input = f"{header_b64}.{payload_b64}".encode("utf-8")
    expected_sig = hmac.new(secret.encode("utf-8"), signing_input, hashlib.sha256).digest()
    expected_b64 = base64.urlsafe_b64encode(expected_sig).decode("utf-8").rstrip("=")
    
    clean_sig = signature_b64.rstrip("=")
    if not hmac.compare_digest(clean_sig, expected_b64):
        raise ValueError("Invalid signature")

    payload_padded = _pad_base64(payload_b64)
    payload = json.loads(base64.urlsafe_b64decode(payload_padded).decode("utf-8"))

    if "exp" in payload:
        if current_time >= payload["exp"]:
            raise ValueError("Token expired")

    return payload

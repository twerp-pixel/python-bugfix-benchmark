import pytest
import base64
import hmac
import hashlib
import json
from ch_10_jwt_validator import validate_jwt

def create_valid_token(payload, secret):
    header = {"alg": "HS256", "typ": "JWT"}
    h_b64 = base64.urlsafe_b64encode(json.dumps(header).encode()).decode().rstrip("=")
    p_b64 = base64.urlsafe_b64encode(json.dumps(payload).encode()).decode().rstrip("=")
    signing_input = f"{h_b64}.{p_b64}".encode()
    sig = hmac.new(secret.encode(), signing_input, hashlib.sha256).digest()
    s_b64 = base64.urlsafe_b64encode(sig).decode().rstrip("=")
    return f"{h_b64}.{p_b64}.{s_b64}"

def test_standard_valid_token():
    token = create_valid_token({"sub": "user_42", "exp": 1000}, "secret123")
    data = validate_jwt(token, "secret123", current_time=500)
    assert data["sub"] == "user_42"

@pytest.mark.edge_case
def test_edge_unpadded_base64_decoding():
    token = create_valid_token({"msg": "hi"}, "secret123")
    data = validate_jwt(token, "secret123", current_time=0)
    assert data["msg"] == "hi"

@pytest.mark.edge_case
def test_edge_expired_at_exact_timestamp():
    token = create_valid_token({"exp": 100}, "secret123")
    with pytest.raises(ValueError, match="Token expired"):
        validate_jwt(token, "secret123", current_time=100)

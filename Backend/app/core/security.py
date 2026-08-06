"""
Security utilities - JWT auth and password hashing
Uses bcrypt for password hashing and HS256 for JWT
"""
import hashlib
import time
import hmac
import base64
import json
from fastapi import HTTPException, Security, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from app.config import settings

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# HTTP Bearer token scheme
bearer_scheme = HTTPBearer(auto_error=False)


def hash_password(password: str) -> str:
    """Hash a password using bcrypt"""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password against its hash"""
    return pwd_context.verify(plain_password, hashed_password)


# Legacy SHA256 support for existing passwords
def verify_password_legacy(password: str, hashed: str) -> bool:
    """Verify password with legacy SHA256 (for migration)"""
    return hmac.compare_digest(hashlib.sha256(password.encode()).hexdigest(), hashed)


def _b64(data: bytes) -> str:
    """Base64 encode without padding"""
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def _b64d(s: str) -> bytes:
    """Base64 decode with padding"""
    pad = 4 - len(s) % 4
    return base64.urlsafe_b64decode(s + "=" * pad)


def create_token(username: str) -> str:
    """Create a JWT token for the user"""
    header = _b64(json.dumps({"alg": "HS256", "typ": "JWT"}).encode())
    payload = _b64(json.dumps({
        "sub": username,
        "exp": int(time.time()) + 60 * 60 * 8,  # 8 hours
        "iat": int(time.time()),
    }).encode())
    sig = _b64(hmac.new(
        settings.secret_key.encode(),
        f"{header}.{payload}".encode(),
        hashlib.sha256,
    ).digest())
    return f"{header}.{payload}.{sig}"


def decode_token(token: str) -> dict:
    """Decode and verify a JWT token"""
    try:
        header, payload, sig = token.split(".")
        expected = _b64(hmac.new(
            settings.secret_key.encode(),
            f"{header}.{payload}".encode(),
            hashlib.sha256,
        ).digest())
        if not hmac.compare_digest(sig, expected):
            raise ValueError("bad signature")
        data = json.loads(_b64d(payload))
        if data["exp"] < time.time():
            raise ValueError("expired")
        return data
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


def get_current_admin(
    creds: HTTPAuthorizationCredentials = Security(bearer_scheme),
):
    """Dependency to get current admin user from JWT token"""
    if not creds:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return decode_token(creds.credentials)
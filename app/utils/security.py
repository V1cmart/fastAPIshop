import hashlib
import bcrypt
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    sha = hashlib.sha256(password.encode()).digest()
    return bcrypt.hashpw(sha, bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    sha256_hash = hashlib.sha256(plain_password.encode()).hexdigest()
    return pwd_context.verify(sha256_hash, hashed_password)

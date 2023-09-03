from passlib.hash import pbkdf2_sha256


def hash_password(password: str):
    return pbkdf2_sha256.hash(password)

def check_password(password: str, hashed: str):
    return pbkdf2_sha256.verify(password, hashed)
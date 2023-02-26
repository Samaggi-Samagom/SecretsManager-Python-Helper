import hashlib

def get_hash(value: str, salt="ssVouchers"):
    return hashlib.sha256((hashlib.sha256(value.encode("utf-8")).hexdigest() + salt).encode("utf-8")).hexdigest()

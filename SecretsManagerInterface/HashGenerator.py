import hashlib


def set_salt(self, salt: str):
    self.__salt = salt


def get(self, value: str, salt: str = None):
    if salt is None:
        salt = self.__salt
    return hashlib.sha256((hashlib.sha256(value.encode("utf-8")).hexdigest() + salt).encode("utf-8")).hexdigest()

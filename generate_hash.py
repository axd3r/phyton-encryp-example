import hashlib
import os
from base64 import b64encode

def generate_django_compatible_hash(password: str, iterations: int = 720000, dklen: int = 32):
    salt = os.urandom(12)

    dk = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        salt,
        iterations,
        dklen
    )

    salt_b64 = b64encode(salt).decode('ascii').strip()
    hash_b64 = b64encode(dk).decode('ascii').strip()

    return f"pbkdf2_sha256${iterations}${salt_b64}${hash_b64}"

def main():
    password = input("Introduce la contraseña: ").strip()
    django_hash = generate_django_compatible_hash(password)
    print("\n✅ Hash compatible con Django:")
    print(django_hash)

if __name__ == "__main__":
    main()

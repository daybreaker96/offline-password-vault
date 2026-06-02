import json
import os
from cryptography.fernet import fernet

KEY_FILE = "vault.key"
DATA_FILE = "vault.json"

def create_key():
  key = Fernet.generate_key()
  with open(KEY_FILE, "wb") as file:
    file.write(key)
  return key

def load_key():
  if not os.path.exists(KEY_FILE):
    return create_key()

  with open(KEY_FILE, "rb") as file:
    return file.read()

def save_vault(data):
  key = load_key()
  fernet = Fernet(key)

  encrypted_data = fernet.encrypt(json.dumps(data).encode())

  with open(DATA_FILE, "wb") as file:
    file.write(encrypted_data)

def load_vault():
  if not os.path.exists(DATA_FILE):
    return []

  key = load_key()
  fernet = Fernet(key)

  with open(DATA_FILE, "rb") as file:
    encrypted_data = file.read()

  decrypted_data = fernet.decrypt(encrypted_data)

  return json.loads(decrypted_data.decode())

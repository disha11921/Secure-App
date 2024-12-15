from cryptography.fernet import Fernet
import os

class SecurityManager:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.save_key()

    def save_key(self):
        with open("encryption_key.key", "wb") as key_file:
            key_file.write(self.key)

    def load_key(self):
        return open("encryption_key.key", "rb").read()

    def encrypt_data(self, data):
        return self.cipher.encrypt(data.encode())

    def decrypt_data(self, encrypted_data):
        return self.cipher.decrypt(encrypted_data).decode()

    def encrypt_file(self, file_path):
        with open(file_path, "rb") as file:
            file_data = file.read()
        encrypted_data = self.cipher.encrypt(file_data)
        return encrypted_data

    def save_encrypted_file(self, file_data, filename):
        os.makedirs("encrypted_data/images", exist_ok=True)
        with open(os.path.join("encrypted_data/images", filename), "wb") as file:
            file.write(file_data)

    def save_password(self, password):
        encrypted_password = self.encrypt_data(password)
        with open("encrypted_data/passwords.txt", "a") as f:
            f.write(encrypted_password.decode() + "\n")

    def retrieve_passwords(self):
        if not os.path.exists("encrypted_data/passwords.txt"):
            return []
        with open("encrypted_data/passwords.txt", "r") as f:
            return [self.decrypt_data(line.strip().encode()) for line in f.readlines()]
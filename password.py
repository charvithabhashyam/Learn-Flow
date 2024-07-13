from cryptography.fernet import Fernet
import json
import os

class PasswordManager:
    def __init__(self, master_password):
        # Generate or load encryption key from master password
        self.key = self.generate_or_load_key(master_password)
        self.cipher_suite = Fernet(self.key)
        self.passwords = {}  # Dictionary to store encrypted passwords
    
    def generate_or_load_key(self, master_password):
        # Generate or load encryption key using master password
        key_file = 'encryption.key'
        if os.path.exists(key_file):
            # Load key if already exists
            with open(key_file, 'rb') as f:
                key = f.read()
        else:
            # Generate key and save to file
            key = Fernet.generate_key()
            with open(key_file, 'wb') as f:
                f.write(key)
        
        # Derive key from master password
        return Fernet(key)

    def encrypt_password(self, password):
        # Encrypt password
        encrypted_password = self.cipher_suite.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        # Decrypt password
        decrypted_password = self.cipher_suite.decrypt(encrypted_password).decode()
        return decrypted_password

    def add_password(self, category, account_name, password):
        # Add password to the manager
        if category not in self.passwords:
            self.passwords[category] = {}
        encrypted_password = self.encrypt_password(password)
        self.passwords[category][account_name] = encrypted_password
        self.save_passwords()

    def get_password(self, category, account_name):
        # Retrieve password from the manager
        if category in self.passwords and account_name in self.passwords[category]:
            encrypted_password = self.passwords[category][account_name]
            decrypted_password = self.decrypt_password(encrypted_password)
            return decrypted_password
        else:
            return None

    def save_passwords(self):
        # Save encrypted passwords to file
        with open('passwords.json', 'w') as f:
            json.dump(self.passwords, f, indent=4)

    def load_passwords(self):
        # Load encrypted passwords from file
        if os.path.exists('passwords.json'):
            with open('passwords.json', 'r') as f:
                self.passwords = json.load(f)

    def generate_strong_password(self, length=12):
        # Generate a strong random password
        import random
        import string
        characters = string.ascii_letters + string.digits + string.punctuation
        strong_password = ''.join(random.choice(characters) for _ in range(length))
        return strong_password


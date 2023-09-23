from cryptography.fernet import Fernet

# Function to generate and store an encryption key in a file
def generate_and_store_key(key_file):
    key = Fernet.generate_key()
    with open(key_file, 'wb') as filekey:
        filekey.write(key)


# Function to encrypt a file using a given key
def encrypt_file(key_file, input_file, output_file):
    with open(key_file, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)

    with open(input_file, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(output_file, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


# Function to decrypt a file using a given key
def decrypt_file(key_file, input_file, output_file):
    with open(key_file, 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)

    with open(input_file, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(output_file, 'wb') as dec_file:
        dec_file.write(decrypted)


# Example usage
if __name__ == "__main__":
    key_file = 'filekey.key'
    input_file = 'nba.csv'
    encrypted_file = 'nba_encrypted.csv'
    decrypted_file = 'nba_decrypted.csv'

    generate_and_store_key(key_file)
    encrypt_file(key_file, input_file, encrypted_file)
    decrypt_file(key_file, encrypted_file, decrypted_file)

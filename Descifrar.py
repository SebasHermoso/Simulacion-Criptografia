from cryptography.fernet import Fernet

# Cargar la clave desde el archivo
with open('key.key', 'rb') as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# Función para descifrar archivos
def decrypt_files(file_path):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()  # Leer los datos cifrados del archivo
    decrypted_data = cipher_suite.decrypt(encrypted_data)  # Descifrar los datos
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)  # Sobrescribir el archivo con los datos descifrados

# Lista de archivos a descifrar (en la vida real, se buscarían de manera recursiva en el sistema)
files_to_decrypt = ['Encriptar.txt', 'Encriptar2.txt']

for file in files_to_decrypt:
    decrypt_files(file)  # Descifrar cada archivo en la lista

print("Archivos descifrados correctamente.")
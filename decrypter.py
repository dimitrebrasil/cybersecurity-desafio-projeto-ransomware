import os
import pyaes

## Abrir arquivo criptografado
file_name = "lista_clientes.txt.ransomwaretroll"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografar
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover arquivo criptografado
os.remove(file_name)

## criar arquivo descriptografado
new_file = "lista_clientes.txt"
new_file = open(f'{new_file}',"wb")
new_file.write(decrypt_data)
new_file.close()

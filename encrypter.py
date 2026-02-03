import os
import pyaes

#leitura do arquivo txt e remocao dele
file_name = 'test.txt'
file = open(file_name, "rb")
file_data = file.read()
file.close()

os.remove(file_name)

#definir a palavra chave e crytografar
key = b"testereansowares"
aes = pyaes.AESModeOfOperationCTR(key)

crypto_data = aes.encrypt(file_data)

#criar o arquivo criptografado
new_file = file_name + ".cryp"

new_file = open(new_file, "wb")
new_file.write(crypto_data)
new_file.close()
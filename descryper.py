import os
import pyaes

#leitura do arquivo e remoçao
file_name = "test.txt.cryp"
file = open(file_name, "rb")
file_data = file.read()
file.close()

os.remove(file_name)

#descriptografar com a chave
key = b"testereansowares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt = aes.decrypt(file_data)

#salvamento da versao descryptografada

new_file = 'text.txt'
new_file = open(new_file, "wb")
new_file.write(decrypt)
new_file.close()
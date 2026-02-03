# Descriptografia de Arquivo com AES (Python)

Este script em Python realiza a **descriptografia de um arquivo criptografado** utilizando o algoritmo **AES em modo CTR**, por meio da biblioteca `pyaes`.

---

## Descrição do Script

O script executa as seguintes etapas:

1. Lê um arquivo criptografado (`test.txt.cryp`) em modo binário.
2. Remove o arquivo criptografado original do sistema.
3. Descriptografa o conteúdo usando uma chave AES pré-definida.
4. Salva o conteúdo descriptografado em um novo arquivo (`text.txt`).

---

## Código

```python
import os
import pyaes

# leitura do arquivo e remoção
file_name = "test.txt.cryp"
file = open(file_name, "rb")
file_data = file.read()
file.close()

os.remove(file_name)

# descriptografar com a chave
key = b"testereansowares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt = aes.decrypt(file_data)

# salvamento da versão descriptografada
new_file = 'text.txt'
new_file = open(new_file, "wb")
new_file.write(decrypt)
new_file.close()

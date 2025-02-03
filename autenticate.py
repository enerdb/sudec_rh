

# Rodar o seguinte comando no bash para converter o arquivo JSON em uma string Base64
# cat credentials.json | base64
# Copie o resutado
# 
# No servidor do streamlit defina uma variável de ambiente chamada GOOGLE_CREDENTIALS e cole a string Base64 gerada.

import os
import json
import base64
import dotenv



# sheet = client.open("Nome da sua Planilha").sheet1
# sheet.append_row(["Nova linha", "com dados"])
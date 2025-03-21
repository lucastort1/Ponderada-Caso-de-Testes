import requests

# URL da API que recebe o atendimento
url = "https://two025-1a-t13-es05-api2.onrender.com/api-docs/index.html" 

# Dados para o atendimento
dados_atendimento = {
    "id_aluno": 12345,
    "id_profissional": 67890,
    "data": "2025-03-21",
    "descricao": "Atendimento psicológico",
}

# Autenticação (exemplo usando token)
headers = {
    "Authorization": "25156486a1e8fdc1ed5e0d9f4b83c18362",
}

# Realizar a requisição POST para registrar o atendimento
response = requests.post(url, json=dados_atendimento, headers=headers)

# Verificar o status da resposta
if response.status_code == 201:
    print("Atendimento registrado com sucesso.")
else:
    print(f"Erro ao registrar atendimento: {response.status_code}")

# Exibir a resposta do servidor
print(response.json())

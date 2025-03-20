import requests

# Parâmetros de configuração
api_url = "https://<sua-instancia>.openai.azure.com/openai/deployments/<seu-deployment>/completions?api-version=2023-03-15-preview"
api_key = "sua_chave_api"

# Dados da solicitação
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}
data = {
    "prompt": "Explique o que é Azure OpenAI de forma simples.",
    "max_tokens": 50,
    "temperature": 0.7,
    "top_p": 1.0
}

# Fazer a chamada
response = requests.post(api_url, headers=headers, json=data)

# Exibir resposta
print(response.json())

import requests

# === CONFIGURAÇÕES ===
usuario = "SEU_USUARIO_GITHUB"            # Ex: "joaosilva"
repositorio = "NOME_DO_REPOSITORIO"       # Ex: "meu-projeto"
token = "SEU_TOKEN_DE_ACESSO"             # Gere em https://github.com/settings/tokens

# === ENDPOINT DA API DO GITHUB ===
url = f"https://api.github.com/repos/{usuario}/{repositorio}"

# === CABEÇALHOS DE AUTENTICAÇÃO ===
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

# === DADOS PARA ALTERAR VISIBILIDADE ===
data = {
    "private": False  # Isso muda de privado para público
}

# === REQUISIÇÃO PATCH PARA ALTERAR O REPOSITÓRIO ===
response = requests.patch(url, headers=headers, json=data)

# === VERIFICAÇÃO DA RESPOSTA ===
if response.status_code == 200:
    print(f"✅ Repositório '{repositorio}' agora é PÚBLICO!")
else:
    print(f"❌ Falha ao alterar a visibilidade.")
    print(f"Código: {response.status_code}")
    print(f"Resposta: {response.text}")

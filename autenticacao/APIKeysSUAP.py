import requests, json, os
from getpass import getpass

api_url = "https://suap.ifrn.edu.br/api/"

def autenticar(api_url):
    user = input("Usuário SUAP: ")
    password = getpass("Senha SUAP: ")

    data = {"username": user, "password": password}
    response = requests.post(api_url + "v2/autenticacao/token/", json=data)

    if response.status_code == 200:
        return response.json()["access"]
    else:
        print(f"Erro ao autenticar: {response.status_code}")
        print("Resposta:", response.json())
        return None

def obterboletim(api_url, token, ano_letivo):
    headers = {
        "Authorization": f'Bearer {token}'
    }
    response = requests.get(f"{api_url}v2/minhas-informacoes/boletim/{ano_letivo}/1", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter boletim: {response.status_code}")
        print("Resposta:", response.json())
        return None

def formatarboletim(boletim):
    print(f"{'Disciplina':<30}{'Média Final':<15}")
    print("=" * 45)

    for disciplina in boletim:
        nome = disciplina.get('disciplina', 'N/A')
        media_final = disciplina.get('media_disciplina', 'N/A')
        media_final_str = str(media_final) if media_final is not None else 'N/A'

        print(f"{nome:<30}{media_final_str:<15}")

def main():
    token = None

    if os.path.exists('suap_keys.json'):
        with open('suap_keys.json', 'r') as file:
            try:
                data = json.load(file)
                token = data.get('token')

                if token:
                    usar_token_existente = input(f"Deseja usar o usuario: ? (s/n): ").strip().lower()
                    if usar_token_existente == 'n':
                        token = None
            except json.decoder.JSONDecodeError:
                pass
    if not token:
        token = autenticar(api_url)
        if token:
            with open('suap_keys.json', 'w') as file:
                json.dump({"token": token}, file)
        else:
            print("Não foi possível obter o token. Verifique suas credenciais.")
            return

    ano_letivo = input("Digite o ano letivo: ")
    boletim = obterboletim(api_url, token, ano_letivo)
    if boletim:
        formatarboletim(boletim)
if __name__ == "__main__":
    main()
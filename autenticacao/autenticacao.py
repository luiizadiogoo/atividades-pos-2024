import requests
from requests.auth import HTTPBasicAuth
from getpass import getpass

def listar_seguidores(auth):
    url = 'https://api.github.com/user/followers'
    response = requests.get(url, auth=auth)
    if response.status_code == 200:
        seguidores = response.json()
        for seguidor in seguidores:
            print(seguidor['login'])
    else:
        print(f"Erro: {response.status_code} - {response.text}")

def seguir_usuario(auth, usuario):
    url = f'https://api.github.com/user/following/{usuario}'
    response = requests.put(url, auth=auth)
    if response.status_code == 204:
        print(f"Você começou a seguir {usuario}.")
    else:
        print(f"Erro: {response.status_code} - {response.text}")

def parar_de_seguir_usuario(auth, usuario):
    url = f'https://api.github.com/user/following/{usuario}'
    response = requests.delete(url, auth=auth)
    if response.status_code == 204:
        print(f"Você parou de seguir {usuario}.")
    else:
        print(f"Erro: {response.status_code} - {response.text}")

def main():
    user = input("Usuário do GitHub: ")
    token = getpass("Token de acesso pessoal GitHub: ")
    
    auth = HTTPBasicAuth(user, token)
    
    while True:
        print("\n1. Listar seguidores")
        print("2. Seguir usuário")
        print("3. Parar de seguir usuário")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            listar_seguidores(auth)
        elif escolha == '2':
            usuario = input("Digite o usuário para seguir: ")
            seguir_usuario(auth, usuario)
        elif escolha == '3':
            usuario = input("Digite o usuário para parar de seguir: ")
            parar_de_seguir_usuario(auth, usuario)
        elif escolha == '4':
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

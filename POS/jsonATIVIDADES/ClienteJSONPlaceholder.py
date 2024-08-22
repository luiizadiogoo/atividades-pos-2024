import requests

API_URL = "https://jsonplaceholder.typicode.com/users"

def listar_usuarios():
    response = requests.get(API_URL)
    if response.status_code == 200:
        usuarios = response.json()
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nome: {usuario['name']}")
    else:
        print("Erro ao listar usuários.")

def listar_tarefas_usuario(user_id):
    response = requests.get(f"{API_URL}/{user_id}/todos")
    if response.status_code == 200:
        tarefas = response.json()
        for tarefa in tarefas:
            status = "Concluída" if tarefa['completed'] else "Pendente"
            print(f"Título: {tarefa['title']}, Status: {status}")
    else:
        print(f"Erro ao listar tarefas com esse ID {user_id}.")

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    username = input("Digite o nome de usuário: ")
    email = input("Digite o email do usuário: ")
    endereco = {
        "street": input("Digite o endereço (rua): "),
        "suite": input("Digite o número do apartamento: "),
        "city": input("Digite a cidade: "),
        "zipcode": input("Digite o CEP: "),
        "geo": {
            "lat": input("Digite a latitude: "),
            "lng": input("Digite a longitude: ")
        }
    }

    usuario = {
        "name": nome,
        "username": username,
        "email": email,
        "address": endereco,
        "phone": input("Digite o telefone: "),
        "website": input("Digite o website: "),
        "company": {
            "name": input("Digite o nome da empresa: "),
            "catchPhrase": input("Digite o slogan da empresa: "),
            "bs": input("Digite o BS da empresa: ")
        }
    }

    response = requests.post(API_URL, json=usuario)
    if response.status_code == 201:
        print("Usuário criado com sucesso!")
    else:
        print("Erro ao criar usuário.")

def ler_usuario(user_id):
    response = requests.get(f"{API_URL}/{user_id}")
    if response.status_code == 200:
        usuario = response.json()
        print(f"ID: {usuario['id']}\nNome: {usuario['name']}\nUsername: {usuario['username']}\nEmail: {usuario['email']}")
        print(f"Endereço: {usuario['address']['street']}, {usuario['address']['city']}")
    else:
        print(f"Erro ao ler usuário com ID {user_id}.")

def atualizar_usuario(user_id):
    usuario = requests.get(f"{API_URL}/{user_id}").json()

    nome = input(f"Nome ({usuario['name']}): ") or usuario['name']
    username = input(f"Nome de usuário ({usuario['username']}): ") or usuario['username']
    email = input(f"Email ({usuario['email']}): ") or usuario['email']
    endereco = {
        "street": input(f"Endereço ({usuario['address']['street']}): ") or usuario['address']['street'],
        "suite": input(f"Suite ({usuario['address']['suite']}): ") or usuario['address']['suite'],
        "city": input(f"Cidade ({usuario['address']['city']}): ") or usuario['address']['city'],
        "zipcode": input(f"CEP ({usuario['address']['zipcode']}): ") or usuario['address']['zipcode'],
        "geo": {
            "lat": input(f"Latitude ({usuario['address']['geo']['lat']}): ") or usuario['address']['geo']['lat'],
            "lng": input(f"Longitude ({usuario['address']['geo']['lng']}): ") or usuario['address']['geo']['lng']
        }
    }

    usuario_atualizado = {
        "name": nome,
        "username": username,
        "email": email,
        "address": endereco,
        "phone": input(f"Telefone ({usuario['phone']}): ") or usuario['phone'],
        "website": input(f"Website ({usuario['website']}): ") or usuario['website'],
        "company": {
            "name": input(f"Empresa ({usuario['company']['name']}): ") or usuario['company']['name'],
            "catchPhrase": input(f"Slogan ({usuario['company']['catchPhrase']}): ") or usuario['company']['catchPhrase'],
            "bs": input(f"BS ({usuario['company']['bs']}): ") or usuario['company']['bs']
        }
    }

    response = requests.put(f"{API_URL}/{user_id}", json=usuario_atualizado)
    if response.status_code == 200:
        print("Usuário atualizado com sucesso!")
    else:
        print(f"Erro ao atualizar usuário com ID {user_id}.")

def deletar_usuario(user_id):
    response = requests.delete(f"{API_URL}/{user_id}")
    if response.status_code == 200:
        print(f"Usuário com ID {user_id} deletado com sucesso!")
    else:
        print(f"Erro ao deletar usuário com ID {user_id}.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Listar todos os usuários")
        print("2. Listar as tarefas de um usuário específico")
        print("3. Criar um usuário")
        print("4. Ler os dados de um usuário")
        print("5. Atualizar os dados de um usuário")
        print("6. Deletar um usuário")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_usuarios()
        elif opcao == "2":
            user_id = input("Digite o ID do usuário: ")
            listar_tarefas_usuario(user_id)
        elif opcao == "3":
            criar_usuario()
        elif opcao == "4":
            user_id = input("Digite o ID do usuário: ")
            ler_usuario(user_id)
        elif opcao == "5":
            user_id = input("Digite o ID do usuário: ")
            atualizar_usuario(user_id)
        elif opcao == "6":
            user_id = input("Digite o ID do usuário: ")
            deletar_usuario(user_id)
        elif opcao == "0":
            print("Saindo")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()
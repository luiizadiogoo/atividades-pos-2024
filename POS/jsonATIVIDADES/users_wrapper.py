import requests

API_URL = "https://jsonplaceholder.typicode.com/users"

def list():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Erro ao listar usuários.")

def create(user_data):
    response = requests.post(API_URL, json=user_data)
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception("Erro ao criar usuário.")

def read(user_id):
    response = requests.get(f"{API_URL}/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao ler usuário com ID {user_id}.")

def update(user_id, user_data):
    response = requests.put(f"{API_URL}/{user_id}", json=user_data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao atualizar usuário com ID {user_id}.")

def delete(user_id):
    response = requests.delete(f"{API_URL}/{user_id}")
    if response.status_code == 200:
        return {"message": f"Usuário com ID {user_id} deletado com sucesso!"}
    else:
        raise Exception(f"Erro ao deletar usuário com ID {user_id}.")

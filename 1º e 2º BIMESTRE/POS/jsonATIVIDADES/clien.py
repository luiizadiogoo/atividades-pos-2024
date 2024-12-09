import users_wrapper as users

def menu():
    while True:
        print("\nMenu:")
        print("1. Listar todos os usuários")
        print("2. Criar um usuário")
        print("3. Ler os dados de um usuário")
        print("4. Atualizar os dados de um usuário")
        print("5. Deletar um usuário")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuarios = users.list()
            for usuario in usuarios:
                print(f"ID: {usuario['id']}, Nome: {usuario['name']}")
        elif opcao == "2":
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

            user_data = {
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

            novo_usuario = users.create(user_data)
            print(f"Usuário criado com sucesso! ID: {novo_usuario['id']}")
        elif opcao == "3":
            user_id = input("Digite o ID do usuário: ")
            try:
                usuario = users.read(user_id)
                print(f"ID: {usuario['id']}\nNome: {usuario['name']}\nUsername: {usuario['username']}\nEmail: {usuario['email']}")
                print(f"Endereço: {usuario['address']['street']}, {usuario['address']['city']}")
            except Exception as e:
                print(e)
        elif opcao == "4":
            user_id = input("Digite o ID do usuário: ")
            try:
                usuario = users.read(user_id)

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

                user_data = {
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

                usuario_atualizado = users.update(user_id, user_data)
                print("Usuário atualizado com sucesso!")
            except Exception as e:
                print(e)
        elif opcao == "5":
            user_id = input("Digite o ID do usuário: ")
            try:
                resultado = users.delete(user_id)
                print(resultado['message'])
            except Exception as e:
                print(e)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()

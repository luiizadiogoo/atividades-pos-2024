import json

def load_json(json_file):
# conteúdo do arquivo JSON
    with open(json_file, 'r', encoding='latin1') as file:
        return json.load(file)

def display_menu(imoveis):
    print("Menu de Imóveis")
    for idx, imovel in enumerate(imoveis):
        print(f"{idx + 1}. {imovel['descricao']}")
    
    while True:
        try:
            escolha = int(input("Digite o número do imóvel para mais detalhes ou 0 para sair: "))
            if escolha == 0:
                print("Saindo...")
                break
            elif 1 <= escolha <= len(imoveis):
                show_details(imoveis[escolha - 1])
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def show_details(imovel):
    print(f"Descrição: {imovel['descricao']}")
    print("Proprietário:")
    print(f"  Nome: {imovel['proprietario']['nome']}")
    if 'email' in imovel['proprietario']:
        print(f"  Email: {imovel['proprietario']['email']}")
    if 'telefone' in imovel['proprietario']:
        print(f"  Telefone(s): {', '.join(imovel['proprietario']['telefone'])}")
    print("Endereço:")
    print(f"  Rua: {imovel['endereco']['rua']}")
    print(f"  Bairro: {imovel['endereco']['bairro']}")
    print(f"  Cidade: {imovel['endereco']['cidade']}")
    print(f"  Número: {imovel['endereco']['numero']}")
    print("Características:")
    print(f"  Tamanho: {imovel['caracteristicas']['tamanho']}")
    print(f"  Número de Quartos: {imovel['caracteristicas']['numQuartos']}")
    print(f"  Número de Banheiros: {imovel['caracteristicas']['numBanheiros']}")
    print(f"Valor: {imovel['valor']}\n")

def main():
    json_file = 'C:/Users/maria/OneDrive/Área de Trabalho/atividades-pos-2024/POS/exemplos/imobiliaria.json'
    try:
        imoveis = load_json(json_file)
        if imoveis:
            display_menu(imoveis)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{json_file}' não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro: Não foi possível decodificar o arquivo JSON.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()

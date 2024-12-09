from xml.dom.minidom import parse

def parse_cardapio(file_path):
    # Carregar e fazer o parse do arquivo XML
    dom = parse(file_path)
    pratos = dom.getElementsByTagName('prato')
    
    # Mostrar o menu com IDs e nomes dos pratos
    print("Menu de Pratos:")
    for prato in pratos:
        prato_id = prato.getAttribute('id')
        nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
        print(f"{prato_id}: {nome}")
    
    # Solicitar ao usuário o ID do prato que deseja saber mais
    prato_id_desejado = input("\nDigite o ID do prato para ver mais detalhes: ")
    
    # detalhes do prato desejado
    for prato in pratos:
        if prato.getAttribute('id') == prato_id_desejado:
            nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
            descricao = prato.getElementsByTagName('descricao')[0].firstChild.nodeValue
            ingredientes = [i.firstChild.nodeValue for i in prato.getElementsByTagName('ingrediente')]
            preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue
            calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue
            tempo_preparo = prato.getElementsByTagName('tempoPreparo')[0].firstChild.nodeValue
            
            print(f"\nDetalhes do Prato {prato_id_desejado}:")
            print(f"Nome: {nome}")
            print(f"Descrição: {descricao}")
            print("Ingredientes:")
            for ingrediente in ingredientes:
                print(f"- {ingrediente}")
            print(f"Preço: {preco}")
            print(f"Calorias: {calorias}")
            print(f"Tempo de Preparo: {tempo_preparo}")
            return
    
    print(f"Prato com ID '{prato_id_desejado}' não encontrado.")

if __name__ == "__main__":
    parse_cardapio("POS/xmlATIVIDADES/cardapio.xml")

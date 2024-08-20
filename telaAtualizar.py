# Ler a base de dados (arquivo) OK
# Utilizar a classe para armazenar os dados OK
# Receber o índice da camiseta a ser atualizada OK
# Atualizar os dados na classe OK
# Reescrever o arquivo
def abrir():
    import csv
    from camiseta import Camiseta
    camisetas = []

    def ler_arquivo():
        with open('camisetas.csv', newline='', encoding='utf-8', errors='ignore') as csvLeitura:
            linha = csv.reader(csvLeitura, delimiter=',')
            for coluna in linha:
                # ARMAZENAR OS PRODUTOS NUMA LISTA
                novaCamiseta = Camiseta(coluna[0], coluna[1], coluna[2], coluna[3], coluna[4], coluna[5])
                camisetas.append(novaCamiseta)




    def altera_dados():
        indice = int(input("Digite o índice do produto a ser alterado:"))
        print("Digite apenas o atributo que você deseja alterar. Caso queira manter o valor antigo, apenas aperte ENTER")
        tamanho = input("Tamanho: ")
        cor = input("Cor: ")
        estilo = input("Estilo: ")
        tecido = input("Tecido: ")
        marca = input("Marca: ")
        preco = input("Preco: ")
        if tamanho != "":
            camisetas[indice].tamanho = tamanho
        if cor != "":
            camisetas[indice].cor = cor
        if estilo != "":
            camisetas[indice].estilo = estilo
        if tecido != "":
            camisetas[indice].tecido = tecido
        if marca != "":
            camisetas[indice].marca = marca
        if preco != "":
            camisetas[indice].preco = preco

    def escreve_arquivo():
        with open('camisetas.csv', 'w', newline='', encoding='utf-8', errors='ignore') as csvEscrita:
            escrever = csv.writer(csvEscrita)
            for c in camisetas:
                escrever.writerow([c.tamanho, c.cor, c.estilo, c.tecido, c.marca, c.preco])
            print(f"Arquivo atualizado! Camisetas atualizada com sucesso!")


    ler_arquivo()
    altera_dados()
    escreve_arquivo()



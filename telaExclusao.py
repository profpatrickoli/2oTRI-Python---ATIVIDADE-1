import csv
linhas = []
indice = int(input("Digite o número da camiseta a ser excluído:"))

# LER ARQUIVO DE PRODUTOS
with open('camisetas.csv', newline='', encoding='utf-8', errors='ignore') as csvLeitura:
    leitor = csv.reader(csvLeitura, delimiter=',')
    for linha in leitor:
        # ARMAZENAR OS PRODUTOS NUMA LISTA
        linhas.append(linha)

#print(linhas)

# REMOVER O "INDICE" DA LISTA
linhas.pop(indice)
#print(linhas)
            
# REESCREVER O ARQUIVO COM A LISTA ATUALIZADA
with open('camisetas.csv', 'w', newline='', encoding='utf-8', errors='ignore') as csvEscrita:
    escrever = csv.writer(csvEscrita)
    escrever.writerows(linhas)
    print(f"Arquivo atualizado! Camiseta {indice} excluída com sucesso!")
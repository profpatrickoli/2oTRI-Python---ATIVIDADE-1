import csv
def abrir():
    with open('camisetas.csv', newline='', encoding='utf-8', errors='ignore') as csvfile:
        leitor = csv.reader(csvfile, delimiter=',')
        for linha in leitor:
            print(f"## Camiseta: {linha[4]}, {linha[2]}, {linha[1]}, Preço: R$ {linha[5]}")

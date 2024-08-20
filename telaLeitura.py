import csv
def abrir():
    i = 0
    with open('camisetas.csv', newline='', encoding='utf-8', errors='ignore') as csvfile:
        leitor = csv.reader(csvfile, delimiter=',')
        for linha in leitor:
            print(f"## Camiseta {i}: {linha[4]}, {linha[3]}, {linha[2]}, {linha[1]}, {linha[0]}, Preço: R$ {linha[5]}")
            i = i+1
import csv
from camiseta import Camiseta

def escreveArquivo(tamanho, cor, estilo, tecido, marca, preco):
    with open('camisetas.csv', 'a', newline='', encoding='utf-8', errors='ignore') as csvfile:
        escreve = csv.writer(csvfile, delimiter=',')
        escreve.writerow([tamanho, cor, estilo, tecido, marca, preco])
        print("### CAMISETA ", marca, "adicionado com sucesso! ###")

camisetas = []
def abrir():
    print("### BEM VINDO A TELA DE CADASTRO DE CAMISETAS ###")
    #while(True):
    print("\nNOVA CAMISETA:")
    tamanho = input("Tamanho: \n")
    cor = input("Cor: \n")
    estilo = input("Estilo: \n")
    tecido = input("Tecido: \n")
    marca = input("Marca: \n")
    preco = input("Preco: \n")
    novaCamiseta = Camiseta(tamanho, cor, estilo, tecido, marca, preco)
    
    escreveArquivo(tamanho, cor, estilo, tecido, marca, preco)
    camisetas.append(novaCamiseta)
    # TESTE PARA VER SE O SISTEMA FUNCIONA:
    print("### LISTA DE CAMISETAS: ###")
    for c in camisetas:
        print(c.marca, c.estilo, c.cor, "- R$", c.preco)

import telaCadastro
import telaLeitura
while(True):
    print("### MENU PRINCIPAL ###")
    print("1 - Cadastrar nova camiseta")
    print("2 - Ver estoque de camisetas")
    opcao = int(input("Digite a opção desejada:"))
    if opcao == 1:
        telaCadastro.abrir()
    elif opcao == 2:
        telaLeitura.abrir()
    else:
        print("Opção inválida")

# CRUD = Create, Read, Update, Delete.
# 1 - cadastrar
# 2 - ler
# 3 - atualizar
# 4 - deletar
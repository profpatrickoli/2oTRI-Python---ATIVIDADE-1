import telaCadastro
import telaLeitura
import telaExclusao
import telaAtualizar

while(True):
    print("### MENU PRINCIPAL ###")
    print("1 - Cadastrar")
    print("2 - Ver estoque")
    print("3 - Excluir")
    print("4 - Alterar")
    opcao = int(input("Digite a opção desejada:"))
    if opcao == 1:
        telaCadastro.abrir()
    elif opcao == 2:
        telaLeitura.abrir()
    elif opcao == 3:
        telaExclusao.abrir()
    elif opcao == 4:
        telaAtualizar.abrir() 
    else:
        print("Opção inválida")

# CRUD = Create, Read, Update, Delete.
# 1 - cadastrar
# 2 - ler
# 3 - deletar
# 4 - atualizar
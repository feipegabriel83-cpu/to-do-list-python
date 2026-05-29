from time import sleep

lista = []
def adicionar_task():
    adicionar = str(input("Digite uma nova tarefa: ")).strip()
    lista.append(adicionar)
def remover_task():
    remover = str(input("Qual tarefa deseja remover? ")).strip()
    if remover not in lista:
        print("Tarefa não encontrada. Tente novamente!")
    else:
        lista.remove(remover)
        print("Tarefa removida com sucesso!!")
def listar_task():
    print(lista)

listar_task()

while True:
    print("""
    [1] - Adicionar Tarefa
    [2] - Remover Tarefa
    [3] - Mostrar Lista
    [4] - Sair
    """)
    opcao = int(input("Digite sua opção: ").strip())
    if opcao == 1:
        adicionar_task()
        print("""Deseja adicionar outra tarefa?
                [1] - SIM
                [2] - NÃO """)
        opcao2 = int(input("Digite sua opção: ").strip())
        if opcao2 == 1:
            adicionar_task()
            listar_task()
        elif opcao2 == 2:
            continue
    elif opcao == 2:
        remover_task()
        listar_task()
        print("""Deseja remover outra tarefa?
                       [1] - SIM
                       [2] - NÃO """)
        opcao2 = int(input("Digite sua opção: "))
        if opcao2 == 1:
            remover_task()
        elif opcao2 == 2:
            continue
    elif opcao == 3:
        listar_task()
    elif opcao == 4:
        listar_task()
        break


print("Encerrando...")
sleep(1)
print("Finalizado!!")

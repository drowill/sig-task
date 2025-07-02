import os


tarefas = {
    1: ["Estudar Programação", True]
}

horarios = {
    "dias": ["Seg", "Ter", "Qua", "Qui", "Sex"],
    "turno": ["M", "T", "N"],
    "hora": ["12","34","56"]
}

agendamentos = {

}


def menuPrincipal():
    os.system("clear")
    print()
    print("""      _________.___  ________        ___________              __    
     /   _____/|   |/  _____/        \__    ___/____    _____|  | __
     \_____  \ |   /   \  ___   ______ |    |  \__  \  /  ___/  |/ /
     /        \|   \    \_\  \ /_____/ |    |   / __ \_\___ \|    < 
    /_______  /|___|\______  /         |____|  (____  /____  >__|__\\""")
    print()
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++         Bem-vindo ao SIG-Task          ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++      1 - Módulo Tarefa                 ++")
    print("++      2 - Módulo Horário                ++")
    print("++      3 - Módulo Agendamento            ++")
    print("++      4 - Módulo Relatório              ++")
    print("++      0 - Sair                          ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    opMain = input("++   Escolha sua opção: ")
    return opMain

def menuTarefa():
    os.system("clear")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++             Módulo Tarefa              ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++      1 - Criar Tarefa                  ++")
    print("++      2 - Exibir dados de Tarefa        ++")
    print("++      3 - Alterar dados de Tarefa       ++")
    print("++      4 - Excluir Tarefa                ++")
    print("++      0 - Voltar ao menu principal      ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    opTarefa = input("++ Escolha sua opcao: ")
    return opTarefa

def criarTarefa():
    os.system('clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++             Criar Tarefa               ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print()
    tarefa = input("++ Tarefa: ")
    print()
    print("++ Tarefa cadastrada")
    tarefas[(len(tarefas)+1)]=[tarefa, True]
    print(tarefas)
    input("Pressione <ENTER>...")

def exibeTarefas():
    os.system('clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++         Exibir dados de Tarefa         ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print()
    id = int(input("++ Insira o id da tarefa: "))
    print()
    print("++ Dados: ", tarefas[id][0])
    input("Pressione <ENTER>...")

def alterarTarefa():
    os.system('clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++         Alterar dados de Tarefa        ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print()
    for id in tarefas:
        print("++ Tarefa", id, ":", tarefas[id][0])
    id = int(input("++ Insira o ID da tarefa que deseja editar: "))
    if id in tarefas:
        novaTarefa = input("++ Insira a nova tarefa: ")
        tarefas[id][0]=novaTarefa
        input("Pressione <ENTER>...")
    else:
        print("Você digitou um id inexistente")
        input("Pressione <ENTER>...")

def excluirTarefa():
    os.system('clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++             Exluir Tarefa              ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print()
    for id in tarefas:
        print("++ Tarefa", id, ":", tarefas[id])
    id = int(input("Insira o ID da tarefa que deseja exluir: "))
    if id in tarefas:
        tarefas[id][1]=False
        print("++ Tarefa exlcuida com sucesso! ")
        input("Pressione <ENTER>...")
    else:
        print("Você digitou um id inexistente")
        input("Pressione <ENTER>...")


def menuAgendamento():
    os.system("clear")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++           Módulo Agendamento           ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++      1 - Criar Agendamento             ++")
    print("++      2 - Exibir dados de Agendamento   ++")
    print("++      3 - Alterar dados de Agendamento  ++")
    print("++      4 - Excluir Agendamento           ++")
    print("++      0 - Voltar ao menu Agendamento    ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    opAgend = input("++ Escolha sua opcao: ")
    return opAgend
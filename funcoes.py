import os

tarefas = {
    1: ["Estudar Programação", True],
    2: ["Arrumar o quarto", True],
    3: ["Dar banho no cachorro", True]
}

horarios = {
    1: {
        "data": "12/12",
        "hora": "12:12",
        "disponivel": True,
        "existe": True
    },
    2: {
        "data": "10/10",
        "hora": "10:10",
        "disponivel": True,
        "existe": True
    },
    3: {
        "data": "1/01",
        "hora": "13:30",
        "disponivel": True,
        "existe": True
    }
}

agendamentos = {}

def sair():
    print()
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++           Programa encerrado           ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print()


def menuPrincipal():
    os.system("clear")
    print()
    print(""" _______  ___   _______         _______  _______  _______  ___   _   
|       ||   | |       |       |       ||   _   ||       ||   | | |  
|  _____||   | |    ___| ____  |_     _||  |_|  ||  _____||   |_| |  
| |_____ |   | |   | __ |____|   |   |  |       || |_____ |      _|  
|_____  ||   | |   ||  |         |   |  |       ||_____  ||     |_   
 _____| ||   | |   |_| |         |   |  |   _   | _____| ||    _  |  
|_______||___| |_______|         |___|  |__| |__||_______||___| |_| """)
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



# TAREFAS


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
    # print(tarefas)
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
    if id in tarefas:
        print("++ Dados: ", tarefas[id][0])
    else:
        print("++ Tarefa nao encontrada")
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
        if tarefas[id][1]:
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
        if tarefas[id][1]:
            print("++ Tarefa", id, ":", tarefas[id][0])
    id = int(input("Insira o ID da tarefa que deseja exluir: "))
    if id in tarefas:
        tarefas[id][1]=False
        print("++ Tarefa exlcuida com sucesso! ")
        input("Pressione <ENTER>...")
    else:
        print("Você digitou um id inexistente")
        input("Pressione <ENTER>...")



# HORARIO


def menuHorario():
    os.system("clear")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++             Módulo Horário             ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++      1 - Criar Horário                 ++")
    print("++      2 - Exibir dados de Horário       ++")
    print("++      3 - Alterar dados de Horário      ++")
    print("++      4 - Excluir Horário               ++")
    print("++      0 - Voltar ao menu principal      ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    opHorario = input("++ Escolha sua opcao: ")
    return opHorario

def criarHorario():
    os.system('clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++             Criar Horário              ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print()
    data = input("++ Data: ")
    hora = input("++ Hora: ")
    disponivel = True
    existe = True
    id = len(horarios)+1
    horarios[id] = {
       "data": data,
       "hora": hora,
       "disponivel": disponivel,
       "existe": existe
    }
    print()
    print("++ Horario criado")
    print(horarios)
    input("Pressione <ENTER>...")

def exibeHorarios():
    os.system('clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++         Exibir dados de Horário        ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print()
    id = int(input("++ Insira o id do horario: "))
    print()
    if id in horarios:
        print("ID\t||\tData\t||\tHora\t||\tDisponivel")
        print(id, end='\t\t')
        print(horarios[id]['data'], end='\t\t')
        print(horarios[id]['hora'], end='\t\t')
        print(horarios[id]['disponivel'])
    else:
        print("ID nao encontrado")
    print()
    input("Pressione <ENTER>...")

def alterarHorario():
    os.system('clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++         Alterar dados de Horário       ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print("++ HORARIOS:                              ++")
    print("ID\t||\tData\t||\tHora\t||\tDisponivel")
    for id in horarios:
        if horarios[id]['existe']:
            print(id, end='\t\t')
            print(horarios[id]['data'], end='\t\t')
            print(horarios[id]['hora'], end='\t\t')
            print(horarios[id]['disponivel'])
    print()
    id = int(input("++ Insira o ID do horário que deseja editar: "))
    if id in horarios:
        data = input("++ Data: ")
        hora = input("++ Hora: ")
        disponivel = True
        existe = True
        horarios[id] = {
            "data": data,
            "hora": hora,
            "disponivel": disponivel,
            "existe": existe
        }
        print()
        print("++ Horario editado")
    else:
        print("Você digitou um id inexistente")

    input("Pressione <ENTER>...")


def excluirHorario():
    os.system('clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++             Exluir Horário             ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print("++ HORARIOS:                              ++")
    print("ID\t||\tData\t||\tHora\t||\tDisponivel")
    for id in horarios:
        if horarios[id]['existe']:
            print(id, end='\t\t')
            print(horarios[id]['data'], end='\t\t')
            print(horarios[id]['hora'], end='\t\t')
            print(horarios[id]['disponivel'])
    id = int(input("Insira o ID da horário que deseja exluir: "))
    if id in horarios:
        horarios[id]['existe']=False
        print("++ Horário excluido com sucesso! ")

    else:
        print("Você digitou um id inexistente")

    input("Pressione <ENTER>...")


# AGENDAMENTO

def menuAgend():
    os.system("clear")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++           Módulo Agendamento           ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++     1 - Criar Agendamento              ++")
    print("++     2 - Exibir dados de Agendamento    ++")
    print("++     3 - Alterar dados de Agendamento   ++")
    print("++     4 - Excluir Agendamento            ++")
    print("++     0 - Voltar ao menu Agendamento     ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    opAgend = input("++ Escolha sua opcao: ")
    return opAgend

def criarAgend():
    os.system("clear")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++           Criar Agendamento            ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++ TAREFAS:                               ++")
    for id in tarefas:
        if tarefas[id][1]:
            print("++ Tarefa", id, ":", tarefas[id][0])
    print("++ HORARIOS:                              ++")
    print("ID\t||\tData\t||\tHora\t||\tDisponivel")
    for id in horarios:
        print(id, end='\t\t')
        print(horarios[id]['data'], end='\t\t')
        print(horarios[id]['hora'], end='\t\t')
        print(horarios[id]['disponivel'])
    print()
    idTarefa = int(input("Insira o ID da tarefa: "))
    idHorario = int(input("Insira o ID do horario: "))
    id = len(agendamentos)+1
    agendamentos[id] = {
        'idTarefa':idTarefa,
        'idHorario':idHorario,
        'existe': True
    }
    print()
    input("Pressione <ENTER>...")


def exibeAgend():
    os.system("clear")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++           Exibir Agendamento           ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print()
    id = int(input("++ Insira o id do agendamento: "))
    if id in agendamentos:
        print("++ AGENDAMENTO:                          ++")
        print("ID\t||\tID da Tarefa\t||\tID do Horario")
        print(id, end='\t\t')
        print(agendamentos[id]['idTarefa'], end='\t\t')
        print(agendamentos[id]['idHorario'])
        print()
    else:
        print("ID nao encontrado")
    input("Pressione <ENTER>...")


def alterarAgend():
    os.system('clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++      Alterar dados de Agendamento      ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print("++ AGENDAMENTOS:                          ++")
    print("ID\t||\tID da Tarefa\t||\tID do Horario")
    for id in agendamentos:
        if agendamentos[id]['existe']:
            print(id, end='\t\t')
            print(agendamentos[id]['idTarefa'], end='\t\t')
            print(agendamentos[id]['idHorario'])
    print()
    id = int(input("++ Insira o ID do agendamento que deseja editar: "))
    if id in agendamentos:
        idTarefa = int(input("Insira o ID da tarefa: "))
        idHorario = int(input("Insira o ID do horario: "))
        agendamentos[id] = {
            'idTarefa':idTarefa,
            'idHorario':idHorario,
            'existe': True
        }
        print()
        print("++ Agendamento editado")
    else:
        print("Você digitou um id inexistente")

    input("Pressione <ENTER>...")


def excluirAgend():
    os.system('clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++      Alterar dados de Agendamento      ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print("++ AGENDAMENTOS:                          ++")
    print("ID\t||\tID da Tarefa\t||\tID do Horario")
    for id in agendamentos:
        if agendamentos[id]['existe']:
            print(id, end='\t\t')
            print(agendamentos[id]['idTarefa'], end='\t\t')
            print(agendamentos[id]['idHorario'])
    print()
    id = int(input("++ Insira o ID do agendamento que deseja excluir: "))
    if id in agendamentos:
        agendamentos[id]['existe']=False
        print("++ Agendamento excluido com sucesso! ")
    else:
        print("++ ID nao encontrado")

    input("Pressione <ENTER>...")


# RELATORIO

def menuRelatorio():
    os.system('clear')
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++            Módulo Relatório            ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++     1 - Lista de tarefas               ++")
    print("++     2 - Lista de horarios              ++")
    print("++     3 - Lista de agendamentos          ++")
    print("++     0 - Voltar                         ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    opRelat = input("++ Escolha sua opcao: ")
    return opRelat

def listaTarefas():
    os.system("clear")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++            Lista de Tarefas            ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print("++ TAREFAS:                              ++")
    print("ID\t||\tTarefa\t||\tExiste")
    for id in horarios:
        print(id, end='\t\t')
        print(tarefas[id][0], end='\t\t')
        print(tarefas[id][1])
    print()
    input("Pressione <ENTER>...")

def listaHorarios():
    os.system("clear")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++            Lista de Horarios           ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print("++ HORARIOS:                              ++")
    print("ID\t||\tData\t||\tHora\t||\tDisponivel\t||\tExiste")
    for id in horarios:
        print(id, end='\t\t')
        print(horarios[id]['data'], end='\t\t')
        print(horarios[id]['hora'], end='\t\t')
        print(horarios[id]['disponivel'], end='\t\t')
        print(horarios[id]['existe'])
    print()
    input("Pressione <ENTER>...")

def listaAgend():
    os.system("clear")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("++                                        ++")
    print("++          Lista de Agendamentos         ++")
    print("++                                        ++")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print()
    print("++ AGENDAMENTOS:                          ++")
    print("ID\t||\tID da Tarefa\t||\tID do Horario\t||\tExiste")
    for id in agendamentos:
        print(id, end='\t\t')
        print(agendamentos[id]['idTarefa'], end='\t\t')
        print(agendamentos[id]['idHorario'], end='\t\t')
        print(agendamentos[id]['existe'])
    print()
    input("Pressione <ENTER>...")
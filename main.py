import funcoes

#########################################
### Agenda de Tarefas e Compromissos  ###
#########################################

# Programa Principal

opMain = ''
while opMain != "0":
    opMain = funcoes.menuPrincipal()
    if opMain == '1':
        opTarefa = ''
        while opTarefa != "0":
            opTarefa = funcoes.menuTarefa()
            if opTarefa == '1':
                funcoes.criarTarefa()
            elif opTarefa == '2':
                funcoes.exibeTarefas()
            elif opTarefa == "3":
                funcoes.alterarTarefa()
            elif opTarefa == '4':
                funcoes.excluirTarefa()
    elif opMain == "2":
        opHorario = ''
        while opHorario != '0':
            opHorario = funcoes.menuHorario()
            if opHorario == '1':
               funcoes.criarHorario()
            elif opHorario == '2':
                funcoes.exibeHorarios()
            elif opHorario == "3":
                funcoes.alterarHorario()
            elif opHorario == '4':
                funcoes.excluirHorario()
    elif opMain == '3':
        opAgend = ''
        while opAgend != '0':
            opAgend = funcoes.menuAgend()
            if opAgend == '1':
                funcoes.criarAgend()
            elif opAgend == '2':
                funcoes.exibeAgend()
            elif opAgend == "3":
                funcoes.alterarAgend()
            elif opAgend == '4':
                funcoes.excluirAgend()
    elif opMain == '4':
        opRelat = ''
        while opRelat != "0":
            opRelat = funcoes.menuRelatorio()
            if opRelat == '1':
                funcoes.listaTarefas()
            elif opRelat == '2':
                funcoes.listaHorarios()
            elif opRelat == "3":
                funcoes.listaAgend()
    elif opMain == '0':
        funcoes.sair()
    else:
        print()
        print("++++++++++++++++++++++++++++++++++++++++++++")
        print("++                                        ++")
        print("++            Opção Inválida!             ++")
        print("++                                        ++")
        print("++++++++++++++++++++++++++++++++++++++++++++")
        print()
        input("Pressione <ENTER>...")


# modulo agendamento
# crud
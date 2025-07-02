import os
import funcoes


#########################################
### Agenda de Tarefas e Compromissos  ###
#########################################


opMain = ''



# Programa Principal

while opMain != "0":
    opMain = funcoes.menuPrincipal()

    if opMain == '1':
        opTarefa = ''
        while opTarefa != "0":
            opTarefa = funcoes.menuTarefa()
            print()
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
            print()
            print("############################################")
            print("#####    Você está no Módulo Horário    ####")
            print("############################################")
            print("#####   1 - Criar Horário              #####")
            print("#####   2 - Exibir dados de Horário    #####")
            print("#####   3 - Alterar dados de Horário   #####")
            print("#####   4 - Excluir Horário            #####")
            print("#####   0 - Voltar ao menu principal   #####")
            opHorario = input("##### Escolha sua opcao: ")
            print()
            if opHorario == '1':
                print()
                print("############################################")
                print("########        Criar Horário       ########")
                print("############################################")
                print()
                horario = input("######## Horário: ")
                print()
                print("####### Tarefa cadastrada")
            elif opHorario == '2':
                print()
                print("############################################")
                print("########   Exibir dados de Horário  ########")
                print("############################################")
                print()
                horario = input("######## Horário: ")
            elif opHorario == "3":
                print()
                print("############################################")
                print("########  Alterar dados de Horário  ########")
                print("############################################")
                print()
                horario = input("######## Horário: ")
            elif opHorario == '4':
                print()
                print("############################################")
                print("########       Excluir Horário      ########")
                print("############################################")
                print()
                horario = input("######## Horário: ")
    elif opMain == '3':
        opAgend = ''
        while opAgend != '0':
            print()
            print("############################################")
            print("#####  Você está no Módulo Agendamento  ####")
            print("############################################")
            print("#####   1 - Criar Agendamento          #####")
            print("#####   2 - Exibir dados de Agendamento ####")
            print("#####   3 - Alterar dados de Agendamento ###")
            print("#####   4 - Excluir Agendamento        #####")
            print("#####   0 - Voltar ao menu principal   #####")
            opAgend = input("##### Escolha sua opcao: ")
            print()
            if opAgend == '1':
                print()
                print("############################################")
                print("########      Criar Agendamento     ########")
                print("############################################")
                print()
                print("######## Tarefas:")
                print("######## Horarios:")
                agendamento = input("######## Agendamento: ")
                print()
                print("####### Tarefa cadastrada")
            elif opAgend == '2':
                print()
                print("############################################")
                print("######## Exibir dados de Agendamento #######")
                print("############################################")
                print()
                agendamento = input("######## Agendamento: ")
            elif opAgend == "3":
                print()
                print("############################################")
                print("######## Alterar dados de Agendamento  #####")
                print("############################################")
                print()
                agendamento = input("######## Agendamento: ")
            elif opAgend == '4':
                print()
                print("############################################")
                print("########     Excluir Agendamento    ########")
                print("############################################")
                print()
                agendamento = input("######## Agendamento: ")
    elif opMain == '4':
        print()
        print("++++++++++++++++++++++++++++++++++++++++++++")
        print("++                                        ++")
        print("++            Módulo Relatório            ++")
        print("++                                        ++")
        print("++++++++++++++++++++++++++++++++++++++++++++")
        input("Tecle <ENTER> para continuar...")
        print()
    elif opMain == '0':
        print()
        print("++++++++++++++++++++++++++++++++++++++++++++")
        print("++                                        ++")
        print("++           Programa encerrado           ++")
        print("++                                        ++")
        print("++++++++++++++++++++++++++++++++++++++++++++")
        print()
    else:
        print()
        print("++++++++++++++++++++++++++++++++++++++++++++")
        print("++                                        ++")
        print("++            Opção Inválida!             ++")
        print("++                                        ++")
        print("++++++++++++++++++++++++++++++++++++++++++++")
        print()
from datetime import datetime
import pickle

agendamentos = {
    # 1: {
    #     "tarefa": "Estudar Programação",
    #     "data":datetime(2025,7,9,14,0),
    #     "concluida": False,
    #     "existe": True
    # },
    # 2: {
    #     "tarefa": "Limpar a casa",
    #     "data":datetime(2025,1,1,14,0),
    #     "concluida": False,
    #     "existe": True
    # }
    
}


try:
    arq_agend = open("agendamentos.dat", "rb")
    agendamentos = pickle.load(arq_agend)
except:
    arq_agend = open("agendamentos.dat", "wb")
arq_agend.close()


if datetime.now() > agendamentos[1]["data"]:
    print("ja passou")
else:
    print("ainda nao")

print(agendamentos)

print(agendamentos[1]['data'].strftime("%X"))




arq_agend = open("agendamentos.dat", "wb")
pickle.dump(agendamentos, arq_agend)
arq_agend.close()
import datetime
import pickle

agendamentos = {}


try:
    arq_agend = open("agendamentos.dat", "rb")
    agendamentos = pickle.load(arq_agend)
except:
    arq_agend = open("agendamentos.dat", "wb")
arq_agend.close()


if datetime.datetime.now() > agendamentos[1]["data"]:
    print("ja passou")
else:
    print("ainda nao")

print(agendamentos)

arq_agend = open("agendamentos.dat", "wb")
pickle.dump(agendamentos, arq_agend)
arq_agend.close()
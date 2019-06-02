#encoding: utf-8
#Nome: Otávio Silveira Munhoz, Daniel Samogin Campioni, Leonardo Vieira von Zuben
#RA: 204280, 214777, 201322
import random
import matplotlib.pyplot


#Atribui a qtd de tentativas;
qtd = 10000
#Vetor com as portas
portas = [1,2,3]
#Vetor que vai armazenar a probabilidade de ganhar se trocou ao longo de todas as tentativas
trocou = []
#Vetor que vai armazenar a probabilidade de ganhar se não trocou ao longo de todas as tentativas
n_trocou =[]
#Var que vai armazenar a probabilidade se trocar na tentiva n
#Var que vai armazenar a probabilidade se não trocar na tentiva n
prob_trocar = 0.0
prob_n_trocar = 0.0
acumulada_troca = 0.0
acumulada_ntroca = 0.0
#Var que vai definir o eixo do gráfico
eixo = []

for i in range(qtd):
    #Escolhe a porta certa e a que o user escolheu
    porta_certa = random.randint(1,3)
    porta_escolhida = random.randint(1,3)
    #Pega a porta livre
    for j in portas:
        if (j!= porta_certa and j!= porta_escolhida):
            porta_mostrar = j
            break
    #Calcula a probabilidade
    if (porta_certa == porta_escolhida):
        prob_n_trocar += 1
    else:
        prob_trocar += 1
    acumulada_ntroca = (prob_n_trocar/(i+1)) * 100
    acumulada_troca = (prob_trocar/(i+1)) * 100
    eixo.append(i+1)
    trocou.append(acumulada_troca)
    n_trocou.append(acumulada_ntroca)
print("Probabilidade caso troque a porta:")
print(acumulada_troca)
print("Probabilidade caso não troque a porta:")
print(acumulada_ntroca)
matplotlib.pyplot.plot(eixo,trocou)
matplotlib.pyplot.title("Probabilidade caso troque a porta:")
matplotlib.pyplot.show()
matplotlib.pyplot.plot(eixo,n_trocou)
matplotlib.pyplot.title("Probabilidade caso nao troque a porta:")
matplotlib.pyplot.show()


#!/usr/bin/env python
# coding: utf-8

# In[28]:


import random
import math
import matplotlib.pyplot


# **Funções que vão gerar a amostra**

# In[29]:


def gerarVetorAmostra(nAmostra):
    vetAmostra = []
    media = 0
    for i in range(2000):
        vetAmostra.append(gerarAmostra(nAmostra, populacao))
        media += vetAmostra[i]
    media = media/len(vetAmostra)
    print("Ok")
    #Enquanto o Ok não for printado significa que ele ainda está gerando os gráficos
    return([vetAmostra,media])


# In[30]:


def gerarAmostra(nAmostra, populacao):
    nVotos = 0.0
    for i in range(nAmostra):
        selecionado = random.randint(0,len(populacao)-1-i) #Gera um número aleatório entre 0 até o total da população - 1 (Vetor vai de 0 até 9999)
        #Eu vou diminuindo o tamanho do vetor que ele pega para não ter reposição
        if (populacao[selecionado] == 0):
            nVotos += 1
        #Coloca a pessoa selecionada no final, na próxima repetição ela é excluida, logo não tem repetição
        aux = populacao[selecionado]
        populacao[selecionado] = populacao[len(populacao)-1-i]
        populacao[len(populacao)-1-i] = aux
    pChapeu = (nVotos/nAmostra) * 100
    return pChapeu


# **Função que gera gráficos**

# In[31]:


def gerarGrafico(vetAmostra, nTotal):
    eixo = [i+1 for i in range(nTotal)]
    matplotlib.pyplot.plot(eixo,vetAmostra)
    matplotlib.pyplot.title("Probabilidade do candidato 1 ser escolhido em uma amostra de tamanho %d" % (nAmostra))
    matplotlib.pyplot.show()


# **Função que calcula o desvio padrão**

# In[32]:


def calcularDesvioPadrao(vetorpChapeu,media):
    somatorio = 0
    for i in vetorpChapeu:
        somatorio += (i - media) * (i - media)
    somatorio = somatorio/1999
    desvioPadrao = math.sqrt(somatorio)
    return desvioPadrao


# **Inicialização das variáveis**

# In[33]:


nVotosCandidatoA = 3000
nVotosCandidatoB = 7000
populacao = []
#Votos no candidato A serão considerados "0's"
for i in range(nVotosCandidatoA):
    populacao.append(0)
#Votos no candidato B serão considerados "1's"
for i in range(nVotosCandidatoB):
    populacao.append(1)
pTotal = nVotosCandidatoA/len(populacao)


# **Gerando a amostra 1**

# In[34]:


nAmostra = 5000
auxVetor = gerarVetorAmostra(nAmostra)
vetAmostra = auxVetor[0]
media = auxVetor[1]


# **Gerando o primeiro gráfico**

# In[35]:


gerarGrafico(vetAmostra, 2000)


# **Exibindo a média e desvio padrão da primeira amostra**

# In[36]:


print("A media da amostra de tamanha %d é: %.2f por cento" %(nAmostra, media))
print("O desvio padrão da amostra de tamanho %d é: %.2f" %(nAmostra, calcularDesvioPadrao(vetAmostra,media)))


# **Amostra 2**

# In[37]:


nAmostra = 200
auxVetor = gerarVetorAmostra(nAmostra)
vetAmostra = auxVetor[0]
media = auxVetor[1]


# **Gerando o segundo gráfico**

# In[38]:


gerarGrafico(vetAmostra, 2000)


# **Exibindo a média e desvio padrão da segunda amostra**

# In[39]:


print("A media da amostra de tamanha %d é: %.2f por cento" %(nAmostra, media))
print("O desvio padrão da amostra de tamanho %d é: %.2f" %(nAmostra, calcularDesvioPadrao(vetAmostra,media)))


# **Comentários**
#     Como é possível observar entre os resultados da amostra 1 e da amostra 2, o desvio padrão da amostra 1 é bem 
#     menor que o da amostra 2, mostrando que os "p chapéus" da amostra 1 se aproximam muito mais do "p real" da 
#     população. Além disso, também é possível observar que os valores de "p chapéu" da amostra 1 variam de 28.5%
#     até 31.5% como mostrado no gráfico refletindo com mais precisão o valor de "p real" do que a da amostra 2, 
#     que varia de 20% até 40%.
#     Logo a amostra 1 tem maior precisão e proximidade com a população total do que a amostra 2, pois a amostra 1 
#     cobre uma quantidade maior de pessoas.

import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib.cbook import boxplot_stats
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler,Normalizer



id_ = [1,2,3,4,5,3,3]
nome = ['João','Tadeu','Maria','Rosa','Henrique','Maria','Maria']
idade = ['20','20','25','25','50','25','25']
altura = [1.6,'1m 70cm',1.8,1.5,'dois metros',1.8,np.nan]
sexo = [' M    ', 'MascuLINO', 'F', 'FeMiNiNo','Masculino','F',np.nan]
peso = [750,71.5,58.2,73.3,82,58.2,np.nan]

dados = {'id':id_,
         'nomes':nome,
         'idade':idade,
         'altura':altura,
         'sexo':sexo,
         'peso':peso}


# Criando DataFrame
dataFrame = pd.DataFrame(dados)

# Devolve uma série booleana informando se cada linha é uma duplicada ou não
#print(dataFrame.duplicated())

#Imprimindo como foi adicionado ao dataframe
#print(dataFrame)

#Se você quiser identificar todas as linhas com o mesmo nome, independentemente das outras colunas, pode fazer assim:
#print(dataFrame.duplicated(subset=['id', 'nomes']))

# Devolve um DataFrame com dados em que o array duplicated é Falso
dataFrame.drop_duplicates()
print(dataFrame)


'''Este método imprime informações sobre um DataFrame incluindo o índice dtype e coluna dtypes, valores não nulos e uso de memória.
 O método info() exibe um resumo técnico do DataFrame, incluindo:
 - O tipo de objeto (classe)
 - O número de linhas e colunas (RangeIndex)
 - O nome e tipo de cada coluna (dtype)
 - Quantos valores não nulos há em cada coluna - E o uso aproximado de memória

dataFrame.info()'''


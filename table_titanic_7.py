import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib.cbook import boxplot_stats
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler,Normalizer


url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

titanic = pd.read_csv(url)

def extrair_titulo(name):

    try:
        parte = name.split(',')[1].strip()
        titulo = parte.split()[0]
        return titulo
    
    except: 
        return None
    
titulos = titanic['Name'].apply(extrair_titulo)
titanic.insert(loc=3, column='Title', value=titulos)



num_reverendos = titanic[titanic['Title'] == 'Rev.'].shape[0]

print(f'Número de passageiros com título "Rev.": {num_reverendos}')

print(titanic.head())
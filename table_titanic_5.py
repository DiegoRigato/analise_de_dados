#Descobrir a distribuição de passageiros entre as classes 1, 2 e 3.

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

titanictrain = pd.read_csv(url)
df = pd.read_csv(url)

titanictrain[['Pclass']].describe()

df["Pclass"].value_counts().plot(kind='bar', color=('purple'))
plt.title("Distribuição de Passageiro por classe")
plt.xlabel("Classe")
plt.ylabel("Quantidade")
plt.show()

#Descobrir se quem sobreviveu era mais jovem ou mais velho.

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

titanictrain = pd.read_csv(url)
df = pd.read_csv(url)

tabela = pd.crosstab(df["Age"], df["Survived"], normalize="index") * 100
print(tabela)

plt.figure(figsize=(14,6))
tabela.plot(kind = "bar", stacked=False ,color=['red', 'blue'], figsize=(14,6))


plt.xlabel("Idade")
plt.ylabel("Percentual (%)")
plt.title("Distribioção percentual de sobrevivencia por idade")
plt.legend(["Não sobreviveu (0)", "Sobrevivel(1)"])
plt.tight_layout()

plt.show()
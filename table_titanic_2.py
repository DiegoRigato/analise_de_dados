#Verificar se passageiros da 1ª classe sobreviveram mais que os da 3ª classe

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

titanictrain = pd.read_csv(url)
df = pd.read_csv(url)

tabela = pd.crosstab(df["Pclass"], df["Survived"], normalize="index") * 100
print(tabela)

df_plot = pd.DataFrame({
    "Nao_Sobreviveu": [37.037037, 52.717391, 75.763747],
    "Sobreviveu": [62.962963, 47.282609, 24.236253]
}, index=[1, 2, 3])

plt.figure(figsize=(8,6))
df_plot.plot(kind="bar")
plt.xlabel("Classe (Pclass)")
plt.ylabel("Percentual (%)")
plt.title("Taxa de Sobrevivência por Classe")
plt.legend(title="Status")
plt.tight_layout()
plt.show()
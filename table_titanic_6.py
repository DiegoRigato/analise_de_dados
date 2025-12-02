#Ver se há alguma tendência entre a idade do passageiro e o valor do bilhete.

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"


titanictrain = pd.read_csv(url)
df = pd.read_csv(url)

bins = [0, 25, 50, 100, 200, 600]
labels = ["0–25", "25–50", "50–100", "100–200", "200+"]
df["FareGroup"] = pd.cut(df["Fare"], bins=bins, labels=labels)

bins = [0, 25, 50, 100]
labels = ["0–25", "25–50", "50–100"]
df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels)


tabela = pd.crosstab(df["FareGroup"], df["AgeGroup"], normalize="index") * 100
print(tabela)

plt.figure(figsize=(14,6))
tabela.plot(kind = 'bar', stacked=False, color = ['pink', 'black', 'purple'], figsize=(14,6))

plt.xlabel("Faixa do valor do bilhete")
plt.ylabel("Percentual dentro da faixa (%)")
plt.title("Distribuição das faixas etárias dentro de cada faixa de valor do bilhete")
plt.legend(title="Faixa de idade")
plt.tight_layout()

plt.show()

#Observar se quem pagou mais caro teve mais chance de sobreviver.

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

tabela = pd.crosstab(df["FareGroup"], df["Survived"], normalize="index") * 100
print(tabela)

plt.figure(figsize=(14,6))
tabela.plot(kind = "bar", stacked=False, color=["green", "black"], figsize=(14,6))

plt.xlabel("Valor do bilhete")
plt.ylabel("Percentual (%)")
plt.title("Distribioção percentual de sobrevivencia por valor do bilhete")
plt.legend(["Não sobreviveu (0)", "Sobrevivel(1)"])
plt.tight_layout()

plt.show()

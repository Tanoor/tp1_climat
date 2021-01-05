# Installation des librairies
from scipy import misc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data_climat = pd.read_excel('./data/Climat.xlsx', header=2, usecols="D:O").iloc[1:32]
df = pd.DataFrame(data_climat)

# Calcul des moyennes par mois
print(np.mean(df))

# Ecart-type par mois
print(np.std(df))

# Minimum par mois
print(df.min())

# Maximum par mois
print(df.max())

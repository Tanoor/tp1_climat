# Installation des librairies
from scipy import misc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def update_annotation(ind):
    x,y = line.get_data()
    annotation.xy = (x[ind["ind"][0]], y[ind["ind"][0]])
    text = year_values[ind["ind"][0]]
    annotation.set_text(text)
    annotation.get_bbox_patch().set_alpha(0.4)

def hover(event):
    vis = annotation.get_visible()
    if event.inaxes == ax:
        cont, ind = line.contains(event)
        if cont:
            update_annotation(ind)
            annotation.set_visible(True)
            fig.canvas.draw_idle()
        else:
            if vis:
                annotation.set_visible(False)
                fig.canvas.draw_idle()

# ------------ Traitement de la feuille SI ------------

data_climat = pd.read_excel('./data/Climat.xlsx', 'SI ', header=2, usecols="D:O").iloc[1:32]
df_climat_SI = pd.DataFrame(data_climat)

# Calcul des moyennes par mois
print(np.mean(df_climat_SI))

# Ecart-type par mois
print(np.std(df_climat_SI))

# Minimum par mois
print(df_climat_SI.min())

# Maximum par mois
print(df_climat_SI.max())

# Affichage des vues mensuelles
month_number = 0
for month in data_climat.head():
    plt.xlabel('Jours de '+month)
    plt.ylabel('Température (°C)')
    plt.plot(df_climat_SI.iloc[:,month_number])
    month_number = month_number+1
    plt.show()

# Affichage de la vue annuelle 
fig, ax = plt.subplots()

year_values = np.concatenate((df_climat_SI.iloc[:, 0], df_climat_SI.iloc[:, 1], df_climat_SI.iloc[:, 2], df_climat_SI.iloc[:, 3], df_climat_SI.iloc[:, 4], df_climat_SI.iloc[:, 5], df_climat_SI.iloc[:, 6], df_climat_SI.iloc[:, 7], df_climat_SI.iloc[:, 8], df_climat_SI.iloc[:, 9], df_climat_SI.iloc[:, 10], df_climat_SI.iloc[:, 11]))
year_values = [x for x in year_values if str(x) != 'nan']
line, = ax.plot(year_values)
ax.set(xlabel='Jour de l\'année', ylabel='Temperature (°C)', title='Evolution de la température sur l\'année')
annotation = ax.annotate("", xy=(0,0), xytext=(-20,20),textcoords="offset points", bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
annotation.set_visible(False)

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show()
plt.show(block=False)

# --------- Traitement de la feuille SI-erreur ---------

data_climat = pd.read_excel('./data/Climat.xlsx', 'SI -erreur', header=2, usecols="D:O").iloc[1:32]
df_climent_SI_erreur = pd.DataFrame(data_climat)

# Suppression des valeurs string en remplaçant pas la moyenne entre la valeur d'avant et celle d'après
for month in range(len(df_climent_SI_erreur.count())):
    for day in range(len(df_climent_SI_erreur.iloc[:, month])):
        if df_climent_SI_erreur.iloc[day, month] == "0xFFFF" or df_climent_SI_erreur.iloc[day, month] == "Sun":
            df_climent_SI_erreur.iloc[day, month] = (df_climent_SI_erreur.iloc[day+1, month] + df_climent_SI_erreur.iloc[day-1, month])/2

for month in range(len(df_climent_SI_erreur.count())):
    avg_month = np.mean(df_climent_SI_erreur.iloc[:, month])
    for day in range(len(df_climent_SI_erreur.iloc[:, month])):
        if np.abs(avg_month-df_climent_SI_erreur.iloc[day, month]) > 20:
            df_climent_SI_erreur.iloc[day, month] = (df_climent_SI_erreur.iloc[day+1, month] + df_climent_SI_erreur.iloc[day-1, month])/2

print(df_climent_SI_erreur)

# Calcul des moyennes par mois
print(np.mean(df_climent_SI_erreur))

# Ecart-type par mois
print(np.std(df_climent_SI_erreur))

# Minimum par mois
print(df_climent_SI_erreur.min())

# Maximum par mois
print(df_climent_SI_erreur.max())

# Affichage des vues mensuelles
month_number = 0
for month in data_climat.head():
    plt.xlabel('Jours de '+month)
    plt.ylabel('Température (°C)')
    plt.plot(df_climent_SI_erreur.iloc[:,month_number])
    month_number = month_number+1
    plt.show()

# Affichage de la vue annuelle 
fig, ax = plt.subplots()

year_values = np.concatenate((df_climent_SI_erreur.iloc[:, 0], df_climent_SI_erreur.iloc[:, 1], df_climent_SI_erreur.iloc[:, 2], df_climent_SI_erreur.iloc[:, 3], df_climent_SI_erreur.iloc[:, 4], df_climent_SI_erreur.iloc[:, 5], df_climent_SI_erreur.iloc[:, 6], df_climent_SI_erreur.iloc[:, 7], df_climent_SI_erreur.iloc[:, 8], df_climent_SI_erreur.iloc[:, 9], df_climent_SI_erreur.iloc[:, 10], df_climent_SI_erreur.iloc[:, 11]))
year_values = [x for x in year_values if str(x) != 'nan']
line, = ax.plot(year_values)
ax.set(xlabel='Jour de l\'année', ylabel='Temperature (°C)', title='Evolution de la température sur l\'année')
annotation = ax.annotate("", xy=(0,0), xytext=(-20,20),textcoords="offset points", bbox=dict(boxstyle="round", fc="w"), arrowprops=dict(arrowstyle="->"))
annotation.set_visible(False)

fig.canvas.mpl_connect("motion_notify_event", hover)

plt.show(block=False)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("comptage_velo_2024.csv", low_memory=False)
df.drop(501288, inplace=True)


def question1():
    print("variables : ", df.columns.tolist())

def question2():
    print("enregistrement : ", len(df.iloc[:,1]))
def question3():
    plus_grand = df["nb_passages"].max()
    print("plus grand nombre vélo comptés : ", plus_grand)
def question4():

    print("vélo total compter : ", df["nb_passages"].sum())
def question5():

    nombre_sections = len(df["id_compteur"].unique())
    print("Nombre de sections différentes : ", nombre_sections)

def question6():
    print(df["heure"].unique())
def graphique1():
    #mettre date + heure en une colonne
    df['dateheure'] = pd.to_datetime(df['date'] + ' ' + df['heure'])
    #nouvelle colonne avec seulement heure
    df['heure2'] = df['dateheure'].dt.hour
    #grouper passage avec l'heure
    hourly_passages = df.groupby('heure2')['nb_passages'].sum().reset_index()
    #afficher le graphique
    hourly_passages.plot(kind='bar', color='darkblue', legend=False, width=0.9)
    plt.title('Nombre total de passages par heure')
    plt.xlabel('Heure')
    plt.ylabel('Nombre total de passages')
    plt.savefig('passage_par_heure.png')
    plt.close()
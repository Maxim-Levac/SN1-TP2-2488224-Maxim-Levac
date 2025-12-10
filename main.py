import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("comptage_velo_2024.csv", low_memory=False)
#enlever ligne avec mauvais format heure
df.drop(501288, inplace=True)
#crée colonne date + heure ensemble, utile pour graphique
df['dateheure'] = pd.to_datetime(df['date'] + ' ' + df['heure'])


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
def graphique2():
    #Prendre la colonne dateheure et garder seulement les mois
    df['Mois_Numero'] = df['dateheure'].dt.month
    mois_dict = {
        1: '1_Janvier', 2: '2_Février', 3: '3_Mars', 4: '4_Avril',
        5: '5_Mai', 6: '6_Juin', 7: '7_Juillet', 8: '8_Août',
        9: '9_Septembre', 10: '10_Octobre', 11: '11_Novembre', 12: '12_Décembre'
    }
    #associer dictionnaire avec map
    df['Mois_Nom'] = df['Mois_Numero'].map(mois_dict)
    #Grouper les mois pour devenir numéro, on prend la première valeur de Mois_nom pour avoir ex 1_janvier, sommation des enregistrement par mois.
    mois_passages = df.groupby('Mois_Numero').agg({'Mois_Nom': 'first', df.columns[3]: 'sum'})

    #graphique
    mois_passages.plot(x='Mois_Nom',kind='bar',legend=False,width=0.8, color='darkblue')
    plt.title('Nombre total de passages par mois')
    plt.xlabel('Mois')
    plt.ylabel('Nombre total de passages')
    plt.savefig('passage_par_mois.png')
    plt.close()
def graphique3():
    df['Heure'] = df['dateheure'].dt.hour
    df['Mois_Numero'] = df['dateheure'].dt.month


    mois_dict = {
        1: 'Jan', 2: 'Fév', 3: 'Mar', 4: 'Avr',
        5: 'Mai', 6: 'Juin', 7: 'Juil', 8: 'Aoû',
        9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Déc'
    }

    #Map les mois
    df['Mois_Abrege'] = df['Mois_Numero'].map(mois_dict)
    #pivot table
    graphique = df.pivot_table(index='Heure',columns='Mois_Abrege',values=df.columns[3],aggfunc='sum')
    #ligne et reste du graphique
    graphique.plot(kind='line', linewidth=1.5)
    plt.title('Nombre total de passages par heure et par mois')
    plt.xlabel('Heure')
    plt.ylabel('Nombre total de passages')
    plt.grid(True, linestyle=':')
    plt.legend(title='Mois')
    plt.savefig('tableau_croisé_dynamique.png')
    plt.close()
def graphique4():
    #regrouper chaque compteur avec sa longitude et latitude, et moyenne de passage dans un tableau
    df_grouped = df.groupby("id_compteur").agg(longitude=('longitude', 'first'),latitude=('latitude', 'first'),moyenne_passages=("nb_passages", 'mean'))

    #graphique avec longitude et latitude come x et y, puis moyenne_passages * 10 comme taille de cercle
    plt.scatter(df_grouped['longitude'],df_grouped['latitude'],s=df_grouped['moyenne_passages'] * 10,alpha=0.5)
    plt.grid(True, linestyle=':')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Localisation des compteurs de vélos\n(taille proportionnelle au nombre moyen de passages)')
    plt.savefig('tableau_croisé_dynamique.png')
    plt.close()
graphique4()
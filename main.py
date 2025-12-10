import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("comptage_velo_2024.csv", low_memory=False)
#enlever ligne avec mauvais format heure
df.drop(501288, inplace=True)
#crée colonne date + heure ensemble, utile pour graphique
df['dateheure'] = pd.to_datetime(df['date'] + ' ' + df['heure'])


def question1():
    """
    Affiche les colonnes

    Retourne :
    string : colonne

    Exemple d'utilisation :
    >>> question1()
    variables :  ['date', 'heure', 'id_compteur', 'nb_passages', 'longitude', 'latitude', 'dateheure']
    """
    #transformer les colonne en liste pour affichage
    print("variables : ", df.columns.tolist())

def question2():
    """
    Affiche le nombre d'enregistrement

    Retourne :
    string : enregistrement + nombre

    Exemple d'utilisation :
    >>> question2()
    enregistrement :  1626014
    """
    #prendre la longueure de n'importe quelle ligne
    print("enregistrement : ", len(df.iloc[:,1]))
def question3():
    """
    Affiche le plus grand nombre d'enregistrement

    Retourne :
    string : enregistrement + information sur enregistrement

    Exemple d'utilisation :
    >>> question3()
    le plus grand nombre d'enregristrement est de  7639.0
               date     heure  latitude  longitude
1146276  2024-09-13  15:45:00   45.5149 -73.607506
    """
    #trouver max enregristrement
    plus_grand = df["nb_passages"].max()
    #associer la ligne ou le max est situé a ligne max
    ligne_max = df[df["nb_passages"] == plus_grand]
    print("le plus grand nombre d'enregristrement est de ",plus_grand)
    print(ligne_max[['date', 'heure', 'latitude', 'longitude']])
def question4():
    """
    Affiche le nombre total de vélo compter

    Retourne :
    string : vélo total compter + nombre

    Exemple d'utilisation :
    >>> question4()
    vélo total compter :  18783319.0
    """
    #somme de la ligne nb_passages au complet
    print("vélo total compter : ", df["nb_passages"].sum())
def question5():
    """
    Affiche le nombre total de section différente

    Retourne :
    string : Nombre de sections différentes + nombre

    Exemple d'utilisation :
    >>> question5()
    Nombre de sections différentes :  56
    """
    #utiliser unique() pour trouver tout les compteurs unique puis afficher le nombre avec len.
    nombre_sections = len(df["id_compteur"].unique())
    print("Nombre de sections différentes : ", nombre_sections)

def question6():
    """
    Affiche une liste de temps unique pour savoir rythme d'enregistrement

    Retourne :
    liste : Temps unique d'enregistrement

    Exemple d'utilisation :
    >>> question6()
    ['00:00:00' '00:15:00' '00:30:00' '00:45:00' '01:00:00' '01:15:00'
 '01:30:00' '01:45:00' '02:00:00' '02:15:00' '02:30:00' '02:45:00'
 '03:00:00' '03:15:00' '03:30:00' '03:45:00' '04:00:00' '04:15:00'
 '04:30:00' '04:45:00' '05:00:00' '05:15:00' '05:30:00' '05:45:00'
 '06:00:00' '06:15:00' '06:30:00' '06:45:00' '07:00:00' '07:15:00'
 '07:30:00' '07:45:00' '08:00:00' '08:15:00' '08:30:00' '08:45:00'
 '09:00:00' '09:15:00' '09:30:00' '09:45:00' '10:00:00' '10:15:00'
 '10:30:00' '10:45:00' '11:00:00' '11:15:00' '11:30:00' '11:45:00'
 '12:00:00' '12:15:00' '12:30:00' '12:45:00' '13:00:00' '13:15:00'
 '13:30:00' '13:45:00' '14:00:00' '14:15:00' '14:30:00' '14:45:00'
 '15:00:00' '15:15:00' '15:30:00' '15:45:00' '16:00:00' '16:15:00'
 '16:30:00' '16:45:00' '17:00:00' '17:15:00' '17:30:00' '17:45:00'
 '18:00:00' '18:15:00' '18:30:00' '18:45:00' '19:00:00' '19:15:00'
 '19:30:00' '19:45:00' '20:00:00' '20:15:00' '20:30:00' '20:45:00'
 '21:00:00' '21:15:00' '21:30:00' '21:45:00' '22:00:00' '22:15:00'
 '22:30:00' '22:45:00' '23:00:00' '23:15:00' '23:30:00' '23:45:00']
    """
    #unique() pour afficher tout les temps unique ce qui montre le rythme d'enregistrement
    print(df["heure"].unique())
def graphique1():
    """
    Fait un graphique pour le nombre total de passage par heure

    Retourne :
    une photo avec format png

    Exemple d'utilisation :
    >>> graphique1()
    passage_par_heure.png
    """
    #nouvelle colonne avec seulement heure
    df['heure2'] = df['dateheure'].dt.hour
    #grouper passage avec l'heure
    hourly_passages = df.groupby('heure2')['nb_passages'].sum()
    #afficher le graphique
    hourly_passages.plot(kind='bar', color='darkblue', legend=False, width=0.9)
    plt.title('Nombre total de passages par heure')
    plt.xlabel('Heure')
    plt.ylabel('Nombre total de passages')
    plt.savefig('passage_par_heure.png')
    plt.close()
def graphique2():
    """
    Fait un graphique pour le nombre total de passage par mois

    Retourne :
    une photo avec format png

    Exemple d'utilisation :
    >>> graphique2()
    passage_par_mois.png
    """
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
    """
    Fait un graphique pour le nombre total de passage par heure et par mois

    Retourne :
    une photo avec format png

    Exemple d'utilisation :
    >>> graphique3()
    tableau_croisé_dynamique.png
    """
    #garder seulement l'heure dans la nouvelle colonne
    df['Heure'] = df['dateheure'].dt.hour
    #garder seuelement les mois dans la nouvelle colonne
    df['Mois_Numero'] = df['dateheure'].dt.month

    #dictionnaire pour raccourci de mois
    mois_dict = {
        1: 'Jan', 2: 'Fév', 3: 'Mar', 4: 'Avr',
        5: 'Mai', 6: 'Juin', 7: 'Juil', 8: 'Aoû',
        9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Déc'
    }

    #Map les mois au numero et faire une nouvelle colonne
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
    """
    Fait un graphique pour la moyenne d'enregistrement comme taille de points et les la latitude et longitude comme coordoné

    Retourne :
    une photo avec format png

    Exemple d'utilisation :
    >>> graphique4()
    nuage_de_points.png
    """
    #regrouper chaque compteur avec sa longitude et latitude, et moyenne de passage dans un tableau
    df_grouped = df.groupby("id_compteur").agg(longitude=('longitude', 'first'),latitude=('latitude', 'first'),moyenne_passages=("nb_passages", 'mean'))

    #graphique avec longitude et latitude come x et y, puis moyenne_passages * 10 comme taille de cercle
    plt.scatter(df_grouped['longitude'],df_grouped['latitude'],s=df_grouped['moyenne_passages'] * 10,alpha=0.5)
    plt.grid(True, linestyle=':')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.title('Localisation des compteurs de vélos\n(taille proportionnelle au nombre moyen de passages)')
    plt.savefig('nuage_de_points.png')
    plt.close()
question1()
question2()
question3()
question4()
question5()
question6()
graphique1()
graphique2()
graphique3()
graphique4()

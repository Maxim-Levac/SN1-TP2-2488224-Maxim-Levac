import pandas as pd
df = pd.read_csv("comptage_velo_2024.csv")

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



question1()
question2()
question3()
question4()
question5()

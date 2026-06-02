import pandas as pd

"""Ce code lit un fichier CSV ou Excel et le convertit en une liste de dictionnaires, 
où chaque dictionnaire représente une ligne du fichier avec les noms de colonnes comme clés."""

def lire_fichier(fichier):

    if fichier.endswith(".csv"):
        df = pd.read_csv(fichier)

    elif fichier.endswith(".xlsx"):
        df = pd.read_excel(fichier)

    else:
        print("Format non supporté")
        return

    data = df.to_dict(orient="records")
    
    return data

data1=lire_fichier(r"C:\Users\Makni\PCA-project\docs\fichier_test.csv")
print(data1)

data2=lire_fichier(r"C:\Users\Makni\PCA-project\docs\fichier_test.xlsx")
print(data2)





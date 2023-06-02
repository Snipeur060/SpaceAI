from func.aianalyze import predict
from rich.console import Console
from func.webinteract import dlimageandreturndata
from func.langage import checklangage
console = Console()
langage = checklangage()

def menu() -> None:
    """
    Affiche le menu
    :return: None
    """
    console.print("Pour quitter le programme, entrez 'stop' ou 'exit'", style="bold blue")
    console.print("Pour changer de modèle, entrez 'low' ou 'high'", style="bold blue")
    console.print("Pour changer d'image, entrez 'non', 'nop' ou 'no'", style="bold blue")
    console.print("Pour continuer, entrez le chemin de l'image", style="bold blue")


while True:
    img_path = console.input(langage["askimgpath"])
    predict_model = 0
    while predict_model != "low" and predict_model != "high":
        predict_model = console.input(langage["modeltouse"])
        #si while toujours pas fini
        if predict_model != "low" and predict_model != "high":
            console.print(langage["wrongvalue"], style="bold red")
    #ajout du support d'une url
    if img_path in ["stop","exit","non","nop","no"]:
        console.print(langage["programstop"], style="bold red")
        exit()
    if img_path.startswith("http"):
        img_data = dlimageandreturndata(img_path)
    else:
        try:
            img_data = open(img_path, 'rb').read()
        except FileNotFoundError:
            console.print(langage["invalidpath"], style="bold red")
            continue
    analyze = predict(img_data, predict_model)
    if "Erreur" in analyze:
        console.print(analyze, style="bold red")
    else:
        console.print(analyze, style="bold green")

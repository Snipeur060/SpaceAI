__VERSION__ = "1.1.0"
__AUTHOR__ = "Snipeur060"

# IMPORT

from func.screenstart import *
from func.aianalyze import predict
from func.webinteract import dlimageandreturndata
from func.langage import checklangage,resetlangage

# INIT

console = Console()
langage = checklangage()

# MAIN

def analyzeimage():
    """
    Analyse une image et affiche le résultat
    :return: Un resultat sous la forme d'une chaine de caractère exemple : "1 Ariane" -> str
    """
    while True:
        console.print(langage["askimgpath"], end="", style="bold blue")
        img_path = console.input()
        predict_model = 0
        while predict_model != "low" and predict_model != "high":
            if img_path in ["stop", "exit", "non", "nop", "no"]:
                console.print(langage["programstop"], style="bold red")
                menu()
            console.print(langage["modeltouse"], end="", style="bold blue")
            predict_model = console.input()
            # si while toujours pas fini
            if predict_model != "low" and predict_model != "high":
                console.print(langage["wrongvalue"], style="bold red")
        # ajout du support d'une url
        if img_path.startswith("http"):
            img_data = dlimageandreturndata(img_path)
        else:
            try:
                img_data = open(img_path, 'rb').read()
            except:
                console.print(langage["invalidpath"], style="bold red")
                continue
        analyze = predict(img_data, predict_model)
        if "Erreur" in analyze:
            console.print(analyze, style="bold red")
        else:
            console.print(analyze, style="bold green")

def menu() -> None:
    global langage
    """
    Affiche le menu, il sert aussi de traitement des inputs pour sélectionner la partie du programme Exemple : 1 -> Analyse d'image, 2 -> Changement de langue etc ...
    :return: None (fait un print / input)
    """
    console.print(langage["menu"], style="bold blue")

    #on demande à l'utilisateur de choisir une option
    while True:
        console.print(langage["chooseoption"], end="", style="bold blue")
        choice = console.input()
        if choice == "1":
            analyzeimage()
            menu()
        elif choice == "2":
            langage = resetlangage()
            menu()
        elif choice == "3":
            console.print("Very Soon...", style="bold red")
            menu()
        elif choice == "4":
            console.print("Credits: Snipeur060", style="bold cyan")
            menu()
        elif choice == "5":
            console.print(langage["programstop"], style="bold red")
            exit()
        elif choice == "6":
            console.clear()
            menu()
        else:
            console.print(langage["wrongvalue"], style="bold red")
            menu()

menu()

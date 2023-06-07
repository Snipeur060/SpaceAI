from rich.console import Console
console = Console()

fr = {
    "askimgpath": "Veuillez entrer le chemin de l'image: ",
    "modeltouse": "Modèle à utiliser (low/high): ",
    "wrongvalue": "Veuillez entrer une valeur correcte",
    "programstop": "Arrêt du programme",
    "invalidpath": "Le chemin de l'image est invalide",
    "urlnotvalid": "L'url n'est pas valide",
    "menu": """ 
    1) Analyser une image
    2) Changer la langue
    3) Vérifier les mises à jour
    4) Voir les crédits
    5) Quitter
    6) Vider la console
    """,
    "chooseoption": "Veuillez choisir une option: ",
    "asklangage": "Veuillez choisir une langue (fr/en): ",
    "resetmessage": "La langue a été réinitialisée. Il faut redémarrer le programme pour que les changements soient pris en compte."
}
en = {
    "askimgpath": "Please enter the path of the image: ",
    "modeltouse": "Model to use (low/high): ",
    "wrongvalue": "Please enter a correct value",
    "programstop": "Program stop",
    "invalidpath": "The path of the image is invalid",
    "urlnotvalid": "The url is not valid",
    "menu": """
    1) Analyze an image
    2) Change language
    3) Check for updates
    4) See credits
    5) Quit
    6) Clear console
    """,
    "chooseoption": "Please choose an option: ",
    "asklangage": "Please choose a language (fr/en): ",
    "resetmessage": "The language has been reset. You have to restart the program for the changes to take effect."
}
console = Console()
def checklangage():
    """
    On ouvre le fichier langage.txt et on récupère la langue
    :return: la langue
    """
    with open("func/langage.txt", "r") as f:
        langage = f.read()
    if langage == "fr" or langage == "en":
        return returnlangage(langage)
    else:
        while True:
            langage = input(en["asklangage"])
            if langage == "fr" or langage == "en":
                break
        with open("func/langage.txt", "w") as f:
            f.write(langage)
        return returnlangage(langage)




def returnlangage(langage):
    """
    Retourne le langage
    :return: le langage
    """
    if langage == "fr":
        return fr
    else:
        return en


def customcheck():
    """
    On ouvre le fichier langage.txt et on récupère la langue
    :return: la langue
    """
    with open("func/langage.txt", "r") as f:
        langage = f.read()
    if langage == "fr" or langage == "en":
        return returnlangage(langage)
    else:
        return en

def resetlangage():
    """
    Reset la langue
    :return: None
    """
    with open("func/langage.txt", "w") as f:
        f.write("None")
    checklangage()
    console.print(en["resetmessage"], style="bold green")

fr = {
    "askimgpath": "Veuillez entrer le chemin de l'image: ",
    "modeltouse": "Modèle à utiliser (low/high): ",
    "wrongvalue": "Veuillez entrer une valeur correcte",
    "programstop": "Arrêt du programme",
    "invalidpath": "Le chemin de l'image est invalide",
}
en = {
    "askimgpath": "Please enter the path of the image: ",
    "modeltouse": "Model to use (low/high): ",
    "wrongvalue": "Please enter a correct value",
    "programstop": "Program stop",
    "invalidpath": "The path of the image is invalid",
}

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
            langage = input("Veuillez entrer une langue valide (fr/en):")
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

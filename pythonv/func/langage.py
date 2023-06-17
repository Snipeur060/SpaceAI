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
    "asklangage": "Veuillez choisir une langue (fr/en/ru): ",
    "resetmessage": "La langue a été réinitialisée"
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
    "asklangage": "Please choose a language (fr/en/ru): ",
    "resetmessage": "The language has been reset"
}


ru = {
    "askimgpath": "Пожалуйста, введите путь к изображению:",
    "modeltouse": "Используемая модель (low/high):",
    "wrongvalue": "Пожалуйста, введите правильное значение",
    "programstop": "Остановка программы",
    "invalidpath": "Путь к изображению недействителен.",
    "urlnotvalid": "URL-адрес недействителен",
    "menu": """ 
    1) Анализатор изображений
    2) Изменить язык
    3) Проверить наличие обновлений
    4) Просмотр кредитов
    5) Сдаться
    6) Очистить консоль
    """,
    "chooseoption": "Пожалуйста, выберите опцию:",
    "asklangage": "Пожалуйста, выберите язык (fr/en/ru): ",
    "resetmessage": "Язык был сброшен"
}

console = Console()
def checklangage():
    """
    On ouvre le fichier langage.txt et on récupère la langue
    :return: la langue
    """
    with open("func/langage.txt", "r") as f:
        langage = f.read()
    if langage == "fr" or langage == "en" or langage == "ru":
        return returnlangage(langage)
    else:
        while True:
            langage = input(en["asklangage"])
            if langage == "fr" or langage == "en" or langage == "ru":
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
    elif langage == "ru":
        return ru
    else:
        return en


def customcheck():
    """
    On ouvre le fichier langage.txt et on récupère la langue
    :return: la langue
    """
    with open("func/langage.txt", "r") as f:
        langage = f.read()
    if langage == "fr" or langage == "en" or langage == "ru":
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
    console.print(en["resetmessage"], style="bold green")
    return checklangage()

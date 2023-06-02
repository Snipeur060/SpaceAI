import requests
import uuid
import shutil
import os
from rich.console import Console
from func.langage import customcheck
console = Console()
lg = customcheck()
def dlimageandreturndata(url):
    """
    Télécharge une image et la retourne sous forme de bytes (selon le format que l'on aura annoncé)
    :param url:
    :return:
    """
    #on va chercher l'image
    try:
        res = requests.get(url, stream=True)
    except requests.exceptions.ConnectionError:
        console.print(lg["urlnotvalid"], style="bold red")
        return False
    #on vérifie que l'url est valide
    if res.status_code == 200:
        #on génère un nom aléatoire pour l'image
        imgname = '/temp/' + str(uuid.uuid4()) + ".png"
        #on sauvegarde l'image
        with open(imgname, 'wb') as f:
            #on copie l'image dans le fichier
            shutil.copyfileobj(res.raw, f)
        #on retourne les données de l'image
        data = open(imgname, 'rb').read()
        #on supprime l'image avec le nom aléatoire
        os.remove(imgname)
        return data
    else:
        console.print(lg["urlnotvalid"], style="bold red")
        return False


def getcontentoffile(url):
    """
    Retourne le contenu d'un fichier
    :param url: url du fichier
    :return:  le contenu du fichier
    """
    res = requests.get(url)
    if res.status_code == 200:
        return str(res.text)
    else:
        console.print(lg["urlnotvalid"], style="bold red")
        return False

import shutil
import uuid
from tkinter import *
from tkinter import messagebox, filedialog,simpledialog
import cv2
import os
import requests

#on désactive les messages d'erreur de tensorflow (ici on cherche à éviter cuda étant donné que l'on a pas besoin de ses infos. Ainsi on se fiche complètement de l'erreur. Il est donc inutile de l'afficher)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from io import BytesIO
from rich.console import Console
import time
lowmodel = load_model('../models/6k_keras_model.h5', compile=False)
highmodel = load_model('../models/18k_keras_model.h5', compile=False)
class_names = open('../models/labels.txt', 'r').readlines()

# Create the root window
root = Tk()
root.title("AI Rocket Finder")

# le titre
title = Label(root, text="AI Rocket Finder", font=("Arial", 20))
title.grid(row=0, column=0, columnspan=3)

#on fait un systeme avec un boutton poru soit choisir un fichier ou soit entrer un lien
file,link = None,None

def open_file():
    global file
    file = filedialog.askopenfilename()
    print(file)

def open_link():
    global link
    link = simpledialog.askstring("Input", "Enter the link", parent=root)
    print(link)


#on fait un boutton pour choisir un fichier
file_button = Button(root, text="Choose a file", command=open_file)
file_button.grid(row=1, column=0)

#on fait un boutton pour entrer un lien
link_button = Button(root, text="Enter a link", command=open_link)
link_button.grid(row=1, column=1)
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
        return False
def predict(imgdata,predict_model):
    global file,link
    if predict_model == "low":
        model = lowmodel
    elif predict_model == "high":
        model = highmodel
    else:
        pass
    try:
        #on récupère le chemin de l'image
        #ici
        #Cela signifie que le tableau a une forme de (1, 224, 224, 3)
        #Ce qui correspond à une image de taille 224x224 avec 3 canaux de couleur (rouge, vert et bleu).
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        # RGBA ce n'est pas possible donc on passe sur dur RGB (suppression du canneau alpha car (rouge, vert et bleu) dans notre array
        # BytesIO ici permet de lire les données de l'image étant donnée que imgdata n'est pas sauvegardé sur le disque il ne pourra pas être lu par PIL (open)
        image = Image.open(BytesIO(imgdata)).convert('RGB')

        #on remet l'image à la bonne taille pour notre tableau
        size = (224, 224)
        #Petite amélioration dans le but d'avoir des données plus clair
        image = ImageOps.fit(image, size, Image.LANCZOS)

        #on fait la transformation image --> Tableau
        image_array = np.asarray(image)
        #encore un petit coup de filtre pour avoir des données "lissé"
        image_array = cv2.GaussianBlur(image_array, (5, 5), 0)

        #Dans le traitement d'image , la normalisation est un processus qui modifie la plage des valeurs d'intensité des pixels.
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

        #On charge la donnée du tableau
        data[0] = normalized_image_array

        # On lance la prédiction avec keras
        prediction = model.predict(data)
        #on v aobtenir l'indice de la classe la plus probable
        index = np.argmax(prediction)
        #on récupère le nom de la classe
        class_name = class_names[index]
        #le score (la probabilité que l'image soit bien class_name)
        confidence_score = prediction[0][index]
        print(class_name)
        return class_name
    except Exception as e:
        print(e)
        return f"""Erreur: {e}"""
    finally:
        file = None
        link = None
def recog(data,predict_model):
    """
    Analyse une image et affiche le résultat
    :return: Un resultat sous la forme d'une chaine de caractère exemple : "1 Ariane" -> str
    """
    img_path = data


    # ajout du support d'une url
    if img_path.startswith("http"):
        img_data = dlimageandreturndata(img_path)
    else:
        try:
            img_data = open(img_path, 'rb').read()
        except:
            pass
        analyze = predict(img_data, predict_model)
        if "Erreur" in analyze:
            print(analyze)
        else:
            print(analyze)



def launchrecognition():
    if (file is not None and file != "") or link is not None:
        print("Recognition launched")
        if file is not None and file != "":
            print("File: ", file)
            recog(file,"low")
        if link is not None:
            print("Link: ", link)
            recog(link,"low")

    else:
        messagebox.showerror("Error", "You must choose a file or enter a link")

#on fait un boutton pour lancer le programme
launch_button = Button(root, text="Launch", command=launchrecognition)
launch_button.grid(row=1, column=2)


# Run the application
root.mainloop()

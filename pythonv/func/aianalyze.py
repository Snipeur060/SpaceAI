import cv2
import os
#on désactive les messages d'erreur de tensorflow (ici on cherche à éviter cuda étant donné que l'on a pas besoin de ses infos. Ainsi on se fiche complètement de l'erreur. Il est donc inutile de l'afficher)
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
from io import BytesIO
from rich.console import Console
import time
console = Console()
if __name__ == '__main__':
  #On doit absolument le lancer dans le fichier main.py en dehors ça ne fonctionne pas
  console.print("Ce script ne peut pas être lancé seul. Ne tentez pas de le lancer seul", style="bold red")
  #on stop tout
  exit()


#on désactive les notations scientifique
np.set_printoptions(suppress=True)

# On charge le modèle
# Ce modèle est le moins évolué (il est par ailleurs le plus rapide)
start_time = time.time()
console.print("Chargement du modèle (6000)...", style="bold blue")
lowmodel = load_model('../models/6k_keras_model.h5', compile=False)
console.print("Le modèle (6k) a été chargé en " + str(round(time.time() - start_time, 2)) + " secondes", style="bold green")

console.print("Chargement du modèle (18000)...", style="bold blue")
highmodel = load_model('../models/18k_keras_model.h5', compile=False)
console.print("Le modèle (18k) a été chargé en " + str(round(time.time() - start_time, 2)) + " secondes", style="bold green")

# Ce modèle est plus évolué entrainé avec +3000 images par class (néanmoins il n'est pas plus lent que le précédent). Par ailleurs le nombre exact d'images est de 18409
#highmodel = load_model('keras_model/high_keras_Model.h5', compile=False)
#les labels (le nom des classes)
class_names = open('../models/labels.txt', 'r').readlines()

def predict(imgdata,predict_model):
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
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

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

    return class_name
  except Exception as e:
    console.print_exception(show_locals=False)
    return f"""Erreur: {e}"""

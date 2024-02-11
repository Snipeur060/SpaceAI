import requests
from bs4 import BeautifulSoup
import os
import uuid
import time
def download_google_images(query, num_images,where):
    url = f"https://www.google.com/search?q={query}&source=lnms&hl=en&tbm=isch&asearch=ichunk&async=_id:rg_s,_pms:s,_fmt:pc&sourceid=chrome&ie=UTF-8"

    # Définir l'en-tête de l'utilisateur pour éviter les blocages
    headers ={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}


    # Récupérer le contenu HTML de la page de recherche Google Images
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Créer un dossier pour sauvegarder les images
    if not os.path.exists(where):
        os.makedirs(where)
    print(soup)
    #on save en local
    with open('test.html', 'w') as f:
        f.write(str(soup))

    # Télécharger les images
    image_tags = soup.find_all('a', class_='rg_l')
    print(image_tags)
    for i, image_tag in enumerate(image_tags[:num_images]):
        image_url = image_tag['href']
        #on enleve /imgres?imgurl=
        image_url = image_url[15:]
        #on cherche &amp; et on degage tout ce qui suit
        image_url = image_url.split("&")[0]

        print(image_url)

        try:
            image_data = requests.get(image_url).content
            time.sleep(1)
            uudd = str(uuid.uuid4())
            with open(f"{where}/image_{uudd}.jpg", 'wb') as f:
                f.write(image_data)
                print(f"Image {uudd} téléchargée avec succès")
        except Exception as e:
            print(f"Impossible de télécharger l'image {i+1} : {e}")

# Exemple d'utilisation
search_query = input("Entrez votre recherche : ")
num_images_to_download = int(input("Combien d'images voulez-vous télécharger ? "))
where = input("Ou voulez vous les télécharger ? ")
download_google_images(search_query, num_images_to_download,where)

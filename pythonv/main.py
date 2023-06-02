from func.aianalyze import predict
from rich.console import Console
from func.webinteract import dlimageandreturndata
console = Console()
while True:
    img_path = console.input("Chemin de l'image: ")
    predict_model = 0
    while predict_model != "low" and predict_model != "high":
        predict_model = console.input("Modèle à utiliser (low/high): ")
        #si while toujours pas fini
        if predict_model != "low" and predict_model != "high":
            console.print("Veuillez entrer une valeur correcte", style="bold red")
    #ajout du support d'une url
    if img_path in ["stop","exit","non","nop","no"]:
        console.print("Arrêt du programme", style="bold red")
        exit()
    if img_path.startswith("http"):
        img_data = dlimageandreturndata(img_path)
    else:
        try:
            img_data = open(img_path, 'rb').read()
        except FileNotFoundError:
            console.print("Le chemin de l'image est invalide", style="bold red")
            continue
    analyze = predict(img_data, predict_model)
    if "Erreur" in analyze:
        console.print(analyze, style="bold red")
    else:
        console.print(analyze, style="bold green")

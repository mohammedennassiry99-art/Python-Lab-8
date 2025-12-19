import utils
from utils import moyenne, est_admis

notes = [12, 9, 15, 8, 17, 13, 19, 10]
prix = 100

# Rapport
rapport = utils.formater_rapport(notes)
print(rapport)

# Moyenne
m = moyenne(notes)
print(f"Moyenne calculée : {m:.2f}")

# Prix TTC
prix_ttc = utils.prix_ttc(prix)
print(f"Prix TTC pour {prix} € HT (taux {utils.TAUX_TVA*100:.0f}%): {prix_ttc:.2f} €")


note_test = 11
print(f"Admis ? {est_admis(note_test)}")

if __name__ == "__main__":
    print("Exécution depuis app.py")

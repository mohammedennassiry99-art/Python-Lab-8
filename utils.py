"""Fonctions utilitaires pour la gestion des notes et du calcul de prix."""

TAUX_TVA = 0.2  # 20 %

def moyenne(notes):
    
    if not notes:
        return 0
    return sum(notes) / len(notes)

def est_admis(note, seuil=10):
 
    return note >= seuil

def prix_ttc(prix_ht, taux=TAUX_TVA):
    
    return prix_ht * (1 + taux)

def formater_rapport(notes):
   
    moyenne_classe = moyenne(notes)
    notes_valides = [note for note in notes if est_admis(note)]
    lignes = [
        "=== Rapport des notes ===",
        f"Notes : {notes}",
        f"Moyenne : {moyenne_classe:.2f}",
        f"Nombre d'etudiants admi : {len(notes_valides)}"
    ]
    return "\n".join(lignes)


if __name__ == "__main__":
    print("Tests rapides de utils.py")
    print(moyenne([10, 12, 14]))

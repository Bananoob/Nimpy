# Fichier principal du jeu de Nim

from nim_logique import (
    appliquer_coup,
    initialiser_tas,
    partie_terminee,
)
from nim_affichage import (
    afficher_regles,
    afficher_tas,
    annoncer_gagnant,
    demander_configuration,
    demander_coup,
    demander_mode_jeu,
    demander_rejouer,
)


def jeu_nim():
    # Lance des parties de Nim à deux joueurs humains.
    afficher_regles()

    while True:
        choix = demander_mode_jeu()
        if choix == 3:
            print("Merci d'avoir joué au jeu de Nim !")
            return

        configuration = [3, 5, 7]
        if choix == 2:
            configuration = demander_configuration()

        tas = initialiser_tas(configuration)
        numero_joueur = 1

        while not partie_terminee(tas):
            afficher_tas(tas)
            numero_tas, nombre_objets = demander_coup(tas, numero_joueur)
            appliquer_coup(tas, numero_tas, nombre_objets)

            if partie_terminee(tas):
                afficher_tas(tas)
                annoncer_gagnant(numero_joueur)
            else:
                numero_joueur = 3 - numero_joueur

        if not demander_rejouer():
            print("Merci d'avoir joué au jeu de Nim !")
            return


# Ce bloc garantit que jeu_nim() ne se lance que si on execute
# directement ce fichier (et non si on l'importe depuis un autre script)
if __name__ == "__main__":
    jeu_nim()

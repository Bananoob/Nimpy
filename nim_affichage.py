# Fichier contenant les fonctions liées à l'affichage

import os

from nim_logique import conseiller_coup, coup_valide


def effacer_console():
    # Efface le terminal avec la commande adaptée au système d'exploitation.
    commande = "cls" if os.name == "nt" else "clear"
    resultat = os.system(commande)
    if resultat != 0:
        raise OSError("Impossible d'effacer la console.")


def afficher_regles():
    # Affiche les règles du jeu au lancement du programme.
    print("=" * 50)
    print("JEU DE NIM")
    print("=" * 50)
    print("A chaque tour, un joueur retire au moins 1 objet")
    print("dans UN SEUL tas de son choix.")
    print("Le joueur qui retire le(s) dernier(s) objet(s) GAGNE.")
    print("Saisissez 'c' au choix du tas pour obtenir un conseil.")
    print("=" * 50)
    print()


def afficher_tas(tas):
    # Affiche les tas et le nombre d'objets restants dans chacun.
    print("\nEtat des tas :")
    for indice, nombre_objets in enumerate(tas):
        symboles = "|" * nombre_objets
        print(f"  Tas {indice} : {symboles}")
    print()


def demander_entier(message):
    # Demande un entier et recommence si la saisie n'est pas valide.
    while True:
        saisie = input(message)
        try:
            valeur = int(saisie)
            return valeur
        except ValueError:
            print("Erreur : veuillez saisir un nombre entier valide.")


def demander_coup(tas, numero_joueur):
    # Demande un coup au joueur et recommence tant que le coup est invalide.
    print(f"--- Tour du joueur {numero_joueur} ---")
    while True:
        saisie_tas = input(
            f"Choisissez un tas (0 a {len(tas) - 1}, ou 'c' pour un conseil) : "
        ).strip().lower()

        if saisie_tas in ("c", "conseil"):
            coup_conseille = conseiller_coup(tas)
            if coup_conseille is None:
                print(
                    "Aucun coup ne garantit la victoire si l'adversaire "
                    "joue parfaitement."
                )
            else:
                numero_conseille, objets_conseilles = coup_conseille
                print(
                    f"Conseil : retirer {objets_conseilles} objet(s) "
                    f"du tas {numero_conseille}."
                )
            continue

        try:
            numero_tas = int(saisie_tas)
        except ValueError:
            print("Saisissez un numéro de tas valide ou 'c' pour un conseil.\n")
            continue

        nombre_objets = demander_entier(
            "Combien d'objets voulez-vous retirer ? "
        )

        if coup_valide(tas, numero_tas, nombre_objets):
            return numero_tas, nombre_objets
        else:
            print("Coup invalide, veuillez recommencer.\n")


def annoncer_gagnant(numero_joueur):
    # Affiche le message de victoire du joueur qui a pris le dernier objet.
    print("=" * 50)
    print(f"Le joueur {numero_joueur} a pris le dernier objet.")
    print(f"BRAVO, le joueur {numero_joueur} GAGNE la partie !")
    print("=" * 50)


def demander_mode_jeu():
    # Propose une configuration classique, personnalisée ou de quitter.
    print("1. Jouer avec la configuration classique (3, 5, 7)")
    print("2. Choisir une configuration")
    print("3. Quitter")

    while True:
        choix = demander_entier("Votre choix : ")
        if choix in (1, 2, 3):
            return choix
        print("Choix invalide. Veuillez choisir 1, 2 ou 3.\n")


def demander_configuration():
    # Demande le nombre de tas et le nombre d'objets dans chacun.
    while True:
        nombre_tas = demander_entier("Combien de tas voulez-vous ? ")
        if nombre_tas >= 1:
            break
        print("Il faut au moins un tas.\n")

    configuration = []
    for indice in range(nombre_tas):
        while True:
            nombre_objets = demander_entier(
                f"Combien d'objets dans le tas {indice} ? "
            )
            if nombre_objets >= 1:
                configuration.append(nombre_objets)
                break
            print("Un tas doit contenir au moins un objet.\n")

    return configuration


def demander_rejouer():
    # Demande si les joueurs souhaitent lancer une nouvelle partie.
    while True:
        reponse = input("Voulez-vous rejouer ? (o/n) ").strip().lower()
        if reponse in ("o", "oui"):
            return True
        if reponse in ("n", "non"):
            return False
        print("Répondez par o (oui) ou n (non).\n")
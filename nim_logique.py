# Fichier liée à la logique du jeu de Nim

def initialiser_tas(configuration=None):
    # Crée et renvoie l'état de départ des tas.
    if configuration is None:
        # Configuration par défaut si aucune n'est fournie
        configuration = [3, 5, 7]
    return list(configuration)


def coup_valide(tas, numero_tas, nombre_objets):
    # Vérifie qu'un coup respecte les règles du jeu.
    # Le numéro de tas doit exister dans la liste
    if numero_tas < 0 or numero_tas >= len(tas):
        return False

    # Le nombre d'objets retirés doit être au moins 1
    if nombre_objets < 1:
        return False

    # On ne peut pas retirer plus d'objets qu'il n'en reste dans le tas
    if nombre_objets > tas[numero_tas]:
        return False

    return True


def appliquer_coup(tas, numero_tas, nombre_objets):
    # Retire les objets d'un tas après avoir vérifié la validité du coup.
    if not coup_valide(tas, numero_tas, nombre_objets):
        raise ValueError("Impossible d'appliquer un coup invalide.")

    tas[numero_tas] -= nombre_objets


def partie_terminee(tas):
    # Indique si tous les tas sont vides.
    return all(nombre_objets == 0 for nombre_objets in tas)


def conseiller_coup(tas):
    # Propose un coup qui laisse une position perdante à l'adversaire si possible.
    somme_nim = 0
    for nombre_objets in tas:
        somme_nim ^= nombre_objets

    if somme_nim == 0:
        return None

    for numero_tas, nombre_objets in enumerate(tas):
        cible = nombre_objets ^ somme_nim
        if cible < nombre_objets:
            return numero_tas, nombre_objets - cible

    return None

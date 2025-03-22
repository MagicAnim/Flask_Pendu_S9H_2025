# unidecode -> évite les problème d'accents => retire les accents
from unidecode import unidecode

# Création d'une classe Pendu
class Pendu :

    # Attributs
    lettres_proposees = []
    mot_a_deviner = ""
    mot_a_afficher = ""
    vies = 0

    #######################################################
    #             1ere Methode : Initialiser              #
    #######################################################
    # Renvoie la data (=état du jeu) correspondante

    def initialiser(mot_a_deviner, vies):
        # On retire les accents et on met le mot en majuscule
        mot_a_deviner = unidecode(mot_a_deviner).upper()

        print("Le mot à deviner est : ", mot_a_deviner )
        # On créer un dictionnaire etat_du_jeu pour monitorer le Pendu
        etat_du_jeu = {
            "lettres_proposees" : [],
            "mot_a_deviner" : mot_a_deviner,
            "mot_a_afficher" : "-" * len(mot_a_deviner),
            "vies": vies,
            "victoire": False,
            "defaite": False,
        }
        # On renvoie notre dictionnqire état du jeu

        return etat_du_jeu
    
    ##################################################
    #              2e METHODE : Deviner              #
    ##################################################
    # On crée notre méthode deviner qui va permettre de réaliser le fonctionnement général du jeu
    def deviner(etat_du_jeu, entree):
        # On récupère toutes nos variables pour les mettre à jour
        global vies 
        global mot_a_deviner
        global mot_a_afficher 
        global lettres_proposees

        # On met à jour toutes les variables de notre classe
        vies = etat_du_jeu["vies"]
        mot_a_deviner = etat_du_jeu["mot_a_deviner"]
        mot_a_afficher = etat_du_jeu["mot_a_afficher"]
        lettres_proposees =etat_du_jeu["lettres_proposees"]

        # Donnéees retournées par deviner()
        data_retour = {
            "victoire" : False,
            "defaite" : False,
            "derniere_entree" : ""
        }
        print(mot_a_afficher)
        # On vérifie si l'utilisateur a tenté un mot ou une lettre
        if len(entree) == 1 :
            message = Pendu.deviner_lettre(entree)
        else: 
            message = Pendu.deviner_mot(entree)

        # On met à jour notre data_retour
        data_retour["vies"] = vies
        data_retour["mot_a_deviner"] = mot_a_deviner
        data_retour["mot_a_afficher"] = mot_a_afficher
        data_retour["lettres_proposees"] = lettres_proposees
        data_retour["message"] = message

        # On vérifie si le joueur a gagné ou perdu
        data_retour["victoire"] = not "-" in mot_a_afficher
        if vies == 0:
           data_retour["defaite"] = True

        # On renvoie nos données du jeu 
        return data_retour


    ##################################################
    #          3e METHODE : Deviner Lettre           #
    ##################################################
    def deviner_lettre(entree):
        global lettres_proposees
        global mot_a_deviner
        global vies
        
        # On vérifie si la lettre a déjà été proposée
        if entree in lettres_proposees:
            return "Tu as déjà proposé cette lettre !!!"
        # Sinon on l'ajoute à liste des lettres proposées
        # On vérifie si elle appartient au mot
        # Si oui on actualise le mot à afficher
        # Sinon on enlève une vie
        else:
            lettres_proposees.append(entree)
            if entree in mot_a_deviner:
                Pendu.actualisation_mot_a_afficher(entree)
                print
                return "Bonne pioche, le mot contient cette lettre !!!"
            else:
                vies -= 1
                return "Oups, cette lettre n'est pas dans le mot !!!"

    ##################################################
    #          4e METHODE : Deviner Mot             #
    ##################################################
    def deviner_mot(entree):
        global mot_a_deviner
        global vies
        global mot_a_afficher

        # On vérifie que l'entree correspond bien au mot à deviner
        if entree == mot_a_deviner:
            mot_a_afficher = entree 
            return "Bravo, tu as trouvé le bon mot !"
        else :
            vies -= 1
            return "Dommage, ce n'est pas le bon mot !"

    ##################################################
    #   5e METHODE : Actualisation du mot à afficher  #
    ##################################################
    # On vérifie si chaque lettre du mot == à l'entrée
    def actualisation_mot_a_afficher(lettre):
        global mot_a_deviner
        global mot_a_afficher
        print(mot_a_afficher)
        # On parcourt grâce à une boucle notre mot_a_deviner
        for i in range(len(mot_a_deviner)):
            # On vérifie dans mot_a_deviner si la lettre est à position i
            if lettre == mot_a_deviner[i] :
                # On passe par une liste car les str sont immuables 
                mot_tmp = list(mot_a_deviner)
                # On ajoute à lettre à la bonne position donc i
                mot_tmp[i] = lettre 
                # On recupe la str avec la methode join
                mot_a_afficher = "".join(mot_tmp)
                print(mot_tmp)

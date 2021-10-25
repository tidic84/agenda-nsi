import pickle


class day():
    """classe créant un objet correspondant
    à une journée : un jour, ce que l'on prévoit de faire/où/quelle h"""

    def __init__(self, jour, activity=[]):
        self.date = jour
        self.event = activity[0]
        self.place = activity[1]
        self.time = activity[2]


def ecrire_dans_l_agenda():
    a = input("Quel jour ?")
    b = input("Que faites-vous ? Où le faites-vous ? A quelle heure le faites-vous ?").split("/")
    jour = day(a, b)
    with open("{}".format(a), "wb") as day_n:
        pickler = pickle.Pickler(day_n)
        pickler.dump(jour.date)
        pickler.dump(jour.event)
        pickler.dump(jour.place)
        pickler.dump(jour.time)


def afficher_lcd():
    pass

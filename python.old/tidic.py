import pickle

class day():
    """classe créant un objet correspondant
    à une journée : un jour, ce que l'on prévoit de faire/où/quelle h"""

    def __init__(self, jour, activity=[]):
        self.date = jour
        self.event = activity[0]
        self.place = activity[1]
        self.time = activity[2]


def add_event(date, event):
    event = event.split("/")
    jour = day(date, event)
    with open("{}".format(date+".event"), "wb") as day_n:
        pickler = pickle.Pickler(day_n)
        pickler.dump(jour.date)
        pickler.dump(jour.event)
        pickler.dump(jour.place)
        pickler.dump(jour.time)
        

def get_event(date):
    with open("{}".format(date+".event"), "rb") as info_n:
        depickler = pickle.Unpickler(info_n)
        paper = []
        for i in range(0,4):
            paper.append(depickler.load())
    return paper
add_event("26-10-2021", "rien/nulle par/16:16")
event = get_event("26-10-2021")
print(event[0])
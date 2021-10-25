import pickle


class day():
    """classe créant un objet correspondant
    à une journée : un jour, ce que l'on prévoit de faire/où/quelle h"""

    def __init__(self, jour, activity=["Rien", "Nulle part", "Jamais"]):
        self.date = jour
        self.event = activity[0]
        self.place = activity[1]
        self.time = activity[2]



j1 = day("25 novembre", ["Mariage de chloé", "Paris", "16h"])

with open("calendar", "wb") as calendar:
    pickler = pickle.Pickler(calendar)
    pickler.dump(j1)

with open("calendar", "rb") as calendar:
    depickler= pickle.Unpickler(calendar)
    déroulement_1 = depickler.load()

print(déroulement_1)
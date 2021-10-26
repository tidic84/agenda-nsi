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
    with open("{}".format("/events/"+date+".event"), "wb") as day_n:
        day_n.write(jour.date + "/")
        day_n.write(jour.event + "/")
        day_n.write(jour.place + "/")
        day_n.write(jour.time)
        

def get_event(date):
    with open("{}".format("/events/"+date+".event"), "rb") as info_n:
        paper = info_n.read()
    return paper

add_event("26-10-2021", "rien/nulle part/16:16")
event = get_event("26-10-2021").split("/")
print(event)
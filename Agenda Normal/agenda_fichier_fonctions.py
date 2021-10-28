import microbit
from time import *

class day():
    """classe créant un objet correspondant
    à une journée : un jour, ce que l'on prévoit de faire/où/quelle h"""

    def __init__(self, jour, activity=[]): # je creer un objet de la class day avec
                                           # les paramètres jour (string) et activity(liste de 4 objets)
        self.date = jour                   # l'objet créé a pour date jour
        self.event = activity[0]           # pour event le premier objet de la liste activity
        self.place = activity[1]           # pour place le deuxieme objet de la liste activity
        self.time = activity[2]            # pour time le troisieme objet de la liste activity
        self.period = activity[3]          # pour period le quatrieme objet de la liste activity


def get_events(date):
  """fonction prenant en parametre la date(str) et retournant les événements du jour date(list)"""
  with open("{}".format(date+".event"), "rb") as info_n:
        paper = info_n.read()
  return paper.split(":")


def get_event(date, n):
  """fonction prenant en parametre la date(str) et le numero de l'événement n(int)
  retournant les caractéristiques de l'événement numero n"""
  with open("{}".format(date+".event"), "rb") as info_n:
        paper = info_n.read()
  return paper.split(":")[n]


def add_event(date, event):
  """fonction prenant en parametres une date(str) et un evenement(list)
  créant un fichier avec la date contenant le nouvel evenement si aucun evenement n'est prevu à cette
  date et ajoutant l'evenement au fichier du jour date si un evenement existe déjà pour celui-ci"""
  try:
    get_events(date)
  except:
    ev = event.split("/")
    jour = day(date, ev)
    with open("{}".format(date+".event"), "wb") as day_n:
      day_n.write(date + ":")
      day_n.write(event)
  else:
    ev = event.split("/")
    jour = day(date, ev)
    with open("{}".format(date+".event"), "ab") as day_n:
        day_n.write(":" + event)

def modifier_event(date, modif, new_data):
    """fonction prenant en parametres une date(str), le numero de l'evenement à modifier(int)
    et la nouvelle valeur de remplacement(str) et remplacant la valeur à modifier par
    la nouvele dans le fichier date"""
    list_1 = get_events(date)
    list_1[modif] = new_data
    #ce que je met à la place
    with open(date+".event", "wb") as nv_fichier:
        nv_fichier.write(":".join(list_1))
        

def supp_event(date, elemsupp):
    """fonction prenant en parametre un date(str) et le numero d'un evenement a supprimer(int)
    puisle supprime du fichier date"""
    list_1 = get_events(date)
    del list_1[elemsupp]
    #j'écris le nv contenu
    with open(date+".event", "wb") as nv_fichier:
        nv_fichier.write(":".join(list_1))

#add_event("27-10-2021","1/2/3/4")
#add_event("27-10-2021","9/0/4/8")
#print(get_events("27-10-2021"))

show_date = mktime(localtime())

def show_events(ts_date):
    """Fonction servant a afficher les évenements d'un jour défini."""
    nrm_date = str(localtime(ts_date).tm_mday)+"-"+str(localtime(ts_date).tm_mon)+"-"+str(localtime(ts_date).tm_year)
    try:
      get_events(nrm_date)
    except:
      print(nrm_date,"Il n'y a pas d'évenemnents ce jour ci")
    else:
      print(nrm_date, "Aujourd'hui,", get_events(show_date))


show_events(show_date)

while True:
    if microbit.button_a.was_pressed():
        show_date -= 86400
        show_events(show_date)
    if microbit.button_b.was_pressed():
        show_date += 86400
        show_events(show_date)
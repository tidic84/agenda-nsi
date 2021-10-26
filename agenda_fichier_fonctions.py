import microbit
from time import *

class day():
    """classe créant un objet correspondant
    à une journée : un jour, ce que l'on prévoit de faire/où/quelle h"""

    def __init__(self, jour, activity=[]):
        self.date = jour
        self.event = activity[0]
        self.place = activity[1]
        self.time = activity[2]
        self.period = activity[3]


def get_events(date):
  with open("{}".format(date+".event"), "rb") as info_n:
        paper = info_n.read()
  return paper.split(":")


def get_event(date, n):
  with open("{}".format(date+".event"), "rb") as info_n:
        paper = info_n.read()
  return paper.split(":")[n]


def add_event(date, event):
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
    list_1 = get_events(date)
    list_1[modif] = new_data
    #ce que je met à la place
    with open(date+".event", "wb") as nv_fichier:
        nv_fichier.write(":".join(list_1))
        

def supp_event(date, elemsupp):
    # quel événement du jour *date* je veux modifier
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
    show_date = str(localtime(ts_date).tm_mday)+"-"+str(localtime(ts_date).tm_mon)+"-"+str(localtime(ts_date).tm_year)
    try:
      get_events(show_date)
    except:
      print(show_date,"Il n'y a pas d'évenemnents ce jour ci")
    else:
      print(show_date, "Aujourd'hui,", get_events(show_date))


show_events(show_date)

while True:
    if microbit.button_a.was_pressed():
        show_date -= 86400
        show_events(show_date)
    if microbit.button_b.was_pressed():
        show_date += 86400
        show_events(show_date)
    
    
    


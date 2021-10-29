from microbit import *
import time
from neopixel import NeoPixel
from projet_nsi_fichier_fonctions import *

nb_led = 31
bandeau_led = NeoPixel(microbit.pin0, nb_led)   # Cree une instance pour piloter 10 WS2812b

dix = Image("90999:""90909:""90909:""90909:""90999:")
onze = Image("90090:""90090:""90090:""90090:""90090:")
douze = Image(  "90090:""90909:""90009:""90090:""90999:")

def showLeds(ts_date):
    """Fonction prenant en parametre le timestamp d'un mois 
    et allume les leds en rouge si il n'y a pas d'évenements,
    en vert si il y a un ou des évenements et ne s'allume pas si il n'y a pas de jour"""
    mois = localtime(ts_date).tm_mon
    year = localtime(ts_date).tm_year
    if dayInMon(ts_date) == 2678400:
        nb_led=31
    elif dayInMon(ts_date) == 2592000:
        nb_led=30
    else:
        nb_led=28
    
    for i in range(1, nb_led+1):
      #print((str(i) + "-" + str(mois) + "-" + str(year)))
        if test_event(str(i) + "-" + str(mois) + "-" + str(year)) == 0:
            bandeau_led[i-1] = (255, 0, 0)  # Configure les Leds en rouge
        else:
            bandeau_led[i-1] = (0, 255, 0)  # Configure les Leds en vert
        if dayInMon(ts_date) == 2592000:
            bandeau_led[30] = (0, 0, 0) # Eteint la dernière led
        elif dayInMon(ts_date) == 2419200:
            for i in range(28, 31):
                bandeau_led[i] = (0, 0, 0) # Eteint la dernière led
      
    bandeau_led.show()  # Affiche toutes les Leds    
    
showLeds(show_date)

while True:
    if microbit.button_a.was_pressed():
        show_date -= dayInMon(show_date)
        showLeds(show_date)
    if microbit.button_b.was_pressed():
        show_date += dayInMon(show_date-dayInMon(show_date))
        showLeds(show_date) 
    
    if localtime(show_date).tm_mon < 10:
        display.show(str(localtime(show_date).tm_mon))
    elif localtime(show_date).tm_mon == 10:
        display.show(dix)
    elif localtime(show_date).tm_mon == 11:
        display.show(onze)
    elif localtime(show_date).tm_mon == 12:
        display.show(douze)

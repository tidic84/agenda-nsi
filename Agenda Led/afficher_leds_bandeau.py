from microbit import *
import time
from neopixel import NeoPixel
from projet_nsi_fichier_fonctions import *

nb_led = 31
bandeau_led = NeoPixel(microbit.pin0, nb_led)   # Cree une instance pour piloter 10 WS2812b

def showLeds(ts_date):
    mois = localtime(ts_date).tm_mon
    year = localtime(ts_date).tm_year
    if dayInMon(ts_date):
      nb_led=31
    else:
      nb_led=30
    for i in range(1, nb_led+1):
      #print((str(i) + "-" + str(mois) + "-" + str(year)))
      if test_event(str(i) + "-" + str(mois) + "-" + str(year)) == 0:
        bandeau_led[i-1] = (255, 0, 0)  # Configure les Leds en rouge
      else:
        bandeau_led[i-1] = (0, 255, 0)  # Configure les Leds en vert
    if dayInMon(ts_date) == False: 
      bandeau_led[30] = (0, 0, 0) # Eteint la dernière led
    bandeau_led.show()  # Affiche toutes les Leds    
    
showLeds(show_date)

while True:
    
    if microbit.button_a.was_pressed():
        show_date -= 2628000
        showLeds(show_date)
        show_events(show_date)  
    if microbit.button_b.was_pressed():
        show_date += 2628000
        showLeds(show_date)  
        show_events(show_date)  


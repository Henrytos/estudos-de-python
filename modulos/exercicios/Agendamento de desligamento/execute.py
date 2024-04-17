#Crie duas funções em python para agendar o desligamento do computador em uma hora e meia hora.
import os
import time

minute = 60

def turn_off_on(minutes):
  print("seu computadir desligara em",minutes)
  time.sleep(minutes*minute)
  os.system("shutdown now")


turn_off_on(1)

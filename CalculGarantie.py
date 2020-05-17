import time
from datetime import date,timedelta
today = date.today()
y = today.year
m = today.month
j = today.day
d = date(y, m, j)
iso=d.isocalendar()
anneepython = iso[0]
anneepython = anneepython - 2000
semainepython = iso[1]
anneedevice = 20
semainedevice = 22
calc1 = anneepython-anneedevice
calc2 = calc1 - 1
if calc1==0:
  delta = semainepython - semainedevice
if calc1==1:
  delta = (52-semainedevice)+semainepython
if calc1>1:
  delta = (52-semainedevice)+semainepython + (calc2 * 52)
if delta > 72 :
  print ("le variateur n'est plus sous garentie")
else:
	  print ("le variateur est sous garentie")
#fin de programme 

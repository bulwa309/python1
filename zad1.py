#lista 1,zadanie 1, zapisywanie punktów do wykresu 
from math import exp

#stałe programu
x0 = 0.0
xk = 5.0
d = 0.1

#funkcja pade1
def z1(x):
    #ta funkcja zwraca znaczenie przybliżenia pade1 od x
    return (6.0-2.0*x)/(6.0+4.0*x+x*x)
#funkcja pade2
def z2(x):
    #ta funkcja zwraca znaczenie przybliżenia pade2 od x
    return (6.0-4.0*x+x*x)/(6.0+2.0*x)

#otwieram plik do zapisywania wyników
with open("zadanie1.txt","w+") as file:
    file.write("#pade.dat\n")
    file.write("#aproksymacja Pade funkcji exp(-x)\n")
    file.write('{:10.3}{:15.8}{:15.8}{:15.8}\n'.format('#x','exp(-x)','z1','z2'))
    x = x0
    while(x<=xk):
        file.write('{:10.3}{:15.8}{:15.8}{:15.8}\n'.format(x,exp(-x),z1(x),z2(x)))
        x += d
		
#dobrze
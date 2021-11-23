import pdb
#ACTIVIDAD 1
from colorama import Style

lista=[[2,6,9],[55,3,10],[2,1,5],[8,6,18]]
pdb.set_trace()

mostrar = [(Style.BRIGHT + str(x))
           if x == max(sublista)
           else x
           for sublista in lista
           for x in sublista]
print(mostrar)

#ACTIVIDAD 2
'''
listaNums = [4,7,9,13,65,8]
primo=c
print(primo)
'''

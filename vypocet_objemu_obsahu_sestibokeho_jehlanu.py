'''
    @Florian Stembera
    - vypocet objemu a obsahu hexajehlanu    
'''

import math

#nacitani vysky telesa
while True:
    h = float(input('výška objektu? '))
    if h<=0:
        print('Vyska telesa nesmi byt mensi nebo rovna nule!')
    else:
        break

#nacitani delky strany telesa
while True:
    s = float(input('délka strany? '))
    if s<=0:
        print('Delka strany telesa nesmi byt mensi nebo rovna nule!')
    else:
        break

#vypocet objemu telesa
V = (math.sqrt(3) / 2) * s ** 2 * h

#vypocet obsahu telesa
P = (3 * math.sqrt(3) / 2) * (s ** 2)
N = ((3 * s) * math.sqrt((h ** 2) + (3 * (s ** 2) / 4)))
S = P + N

#zobrazeni vyslednych hodnot
print('objem objektu je %.2f' % V)
print('obsah objektu je %.2f' % S)


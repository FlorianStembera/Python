#kalkulacka - objem a obsah hexapyramid

import math

h = float(input('vyska telesa? '))

while  h <= 0:
    print('Vyska telesa nesmi byt mensi nebo rovna nule!')
    h = float(input('výška objektu? '))

s = float(input('delka strany telesa? '))

while s <= 0:
    print('Delka strany telesa nesmi byt mensi nebo rovna nule!')
    s = float(input('délka strany? '))

#objem objektu

V = (math.sqrt(3) / 2) * s ** 2 * h

#obsah objektu

P = (3 * math.sqrt(3) / 2) * (s ** 2)
N = ((3 * s) * math.sqrt((h ** 2) + (3 * (s ** 2) / 4)))
S = P + N

print('objem objektu je %.2f' % V)
print('obsah objektu je %.2f' % S)


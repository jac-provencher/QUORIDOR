from itertools import chain
from more_itertools import intersperse, flatten

etat = {
"joueurs": [
    {"nom": "idul", "murs": 7, "pos": [5, 6]},
    {"nom": "automate", "murs": 3, "pos": [5, 7]}
],
"murs": {
    "horizontaux": [[4, 4], [2, 6], [3, 8], [5, 8], [7, 6]],
    "verticaux": [[6, 2], [4, 4], [2, 5], [7, 5], [7, 7], [10, 3]]
}
}


def afficher_damier_ascii(gamestate):
    """
    Afficher le damier en ASCII
    :returns: chaine de caractère
    """
    # Construction du damier
    damier = [['.' if x % 4 == 0 else ' ' for x in range(39)] if y % 2 == 0 else [' ' for x in range(39)] for y in range(17)]
    for i, line in enumerate(damier[::2]):
        line[0] = str(9-i)
    for line in damier:
        line[2] = line[-1] = '|'
    # Position des joueurs
    for i in range(2):
        x, y = gamestate['joueurs'][i]['pos']
        damier[(9-y)*2][x*4] = str(i+1)
    # Murs horizontaux
    for x, y in gamestate['murs']['horizontaux']:
        for i in range(7):
            damier[(9-y)*2+1][x*4+i-1] = '-'
    # Murs verticaux
    for x, y in gamestate['murs']['verticaux']:
        damier[(9-y)*2][x*4-2] = damier[(9-y)*2-1][x*4-2] = damier[(9-y)*2-2][x*4-2] = '|'

    return '\n'.join(''.join(spot for spot in line) for line in damier) # ''.join(intersperse('\n', flatten(damier), n=39))

"""
Voici ce qu'on obtient lorsqu'on print,

9 | .   .   .   .   .   .   .   .   . |
  |                                   |
8 | .   .   .   .   .   . | .   .   . |
  |        ------- -------|           |
7 | .   .   .   .   2   . | .   .   . |
  |                                   |
6 | . | .   .   .   1   . | .   .   . |
  |   |-------            |-------    |
5 | . | .   . | .   .   . | .   .   . |
  |           |                       |
4 | .   .   . | .   .   .   .   .   . |
  |            -------                |
3 | .   .   .   .   . | .   .   .   . |
  |                   |               |
2 | .   .   .   .   . | .   .   .   . |
  |                                   |
1 | .   .   .   .   .   .   .   .   . |

"""
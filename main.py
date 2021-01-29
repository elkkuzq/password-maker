import random
import string

nimet = ['Rick','Jerry','Morty',
         'Meese','Cop','Rixty',
         'Birdperson','Unity']

adjectives = ['Doofus','stupid','Dumb',
              'Fool','PIECEOFSHIT',
              'Brainless','crazy','nuts', 'genius', 'smart', 'smartest person']

print('you cant make own password? I tell you why. YOU ARE PIECE OF SHIT!')

while (True):
    for num in range(1, 4):
        name = random.choice(nimet)
        adjective = random.choice(adjectives)
        number = random.randrange(0, 138)
        """char = random.choice(string.punctuation) if you want put punctuation"""

        password = name + adjective + str(number)
        
        print ('Password for person', num, 'is', password)
    still = input('you still want new password? (Y/N)')
    if still.lower == 'n'.lower or still.lower == 'N'.lower:
        break

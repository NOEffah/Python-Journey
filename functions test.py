from functions import make_pizza as mp  # implementing import, from and aliases(short version recognisable in this file)

mp(13, 'banu')
mp(12, 'mushroom', 'banky')


# alias extra example
import functions as p

p.make_album('Kofi', 'Dance')

# to reference every function
from functions import *
make_pizza(13, 'banu')

unprinted_designes = ['phone case', 'robot pendant', 'dodecahedron']
completed_modes = []

print_models(unprinted_designes,completed_modes)
show_completed_models(completed_modes)



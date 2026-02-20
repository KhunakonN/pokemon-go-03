types = [
    'Water','Fire','Bug','Steel','Dark',
    'Dragon','Electric','Fairy','Fighting','Flying',
    'Ghost','Grass','Ground','Ice','Normal',
    'Poison','Psychic','Rock'
]

from pokemon.model import Type
pokemon_types = [Type(name=pt) for pt in types]
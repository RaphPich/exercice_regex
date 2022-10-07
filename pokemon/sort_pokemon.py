import unittest

import yaml

from pokemon.pokedex import Pokedex

class TestPokemon(unittest.TestCase):
    """comment

    """
    def test_pokemon_dict(self) -> None:
        with open("pokemon/pokemon.yaml") as file:
            golden_pokemon = yaml.load(file, Loader=yaml.FullLoader)
        pokedex = Pokedex()
        self.assertEqual(golden_pokemon, pokedex.data)

if __name__ == '__main__':
    unittest.main()
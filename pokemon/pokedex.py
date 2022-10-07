import re
import yaml

with open("pokemon/pokemon.html", "r") as file:
    content = file.read()

regex = re.compile(r'href="(\S+)"\s.*title="(\S+)"')
pokedex = {line[1]: line[0] for line in regex.findall(content, re.MULTILINE)}

with open('pokemon/pokemon.yaml', 'w') as file:
    yaml.dump(pokedex, file)

class Pokedex:
    def __init__(self) -> None:
        with open("pokemon/pokemon.html", "r") as file:
            content = file.read()
        regex = re.compile(r'href="(\S+)"\s.*title="(\S+)"')
        self.data = {line[1]: line[0] for line in regex.findall(content, re.MULTILINE)}
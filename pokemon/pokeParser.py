import re

pokedex = open("pokemon\\pokemon.html")

regex = re.compile("href=\"(/wiki/\w+)\" class=\".+\" title=\"(\w+)\"")

pokedict = {}
i = 0

for match in re.finditer(regex, pokedex.read()):
    i += 1
    pokedict[match.group(2)] = {"link":match.group(1), "number":i}

print(pokedict)

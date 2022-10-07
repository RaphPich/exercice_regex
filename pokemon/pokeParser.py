import re

pokedex = open("pokemon\\pokemon.html")
regex = re.compile("href=\"(/wiki/\w+)\".+title=\"(\w+)\"")

pokedict = {match.group(2):{"link":match.group(1),"number":i} for i, match in enumerate(re.finditer(regex, pokedex.read()))}

print(pokedict)

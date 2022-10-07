import re

file = open("pokemon/pokemon.html", "r")

texte = file.read()

file.close()

regexp = re.compile(r"<td[^>]+>(\d+)\n?\s+</td>\n?\s+?\n?\s+<td(?:[^>]+)?><a href=\"([^\"]+)\".+title=\"([^\"]+)\">")

res = re.findall(regexp, texte)

for k in res:
    print("Pokemon n°", k[0], "->", k[2], "\t\thttps://fr.wikipedia.org"+ k[1])
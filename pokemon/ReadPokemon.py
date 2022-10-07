from cmath import polar
import re
import codecs

def dictPokemon():

    pokeFile = codecs.open("pokemon.html", "r", "utf-8").read()
    pokemonNameRegex = re.compile('href=\"(.*?)\".*title=\"(\w*)\"')
    pokeList = pokemonNameRegex.findall(pokeFile)
    
    pokeDict = {}
    for i in range(len(pokeList)):
        pokeDict[pokeList[i][1]]=pokeList[i][0]
    
    print(pokeDict)
    

dictPokemon()
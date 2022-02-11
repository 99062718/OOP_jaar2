from pokeLib import *

pokemons = {}

def pokeAttack(nameAttacker, nameAttacked, attack):
    print(f"{nameAttacked} has {pokemons[nameAttacked].getStat('health')} hp")
    print(f"{nameAttacker} uses {attack[0]} on {nameAttacked}")
    pokemons[nameAttacked].takeDamage(attack[1], pokemons[nameAttacker].getStat("energyType"))
    print(f"{nameAttacked} has {pokemons[nameAttacked].getStat('health')} hp")

pokemons["pikachu"] = pokemon("pikachu", "lightning", 60, {"electric ring": 50, "pika punch": 20}, [["fighting", 2]], [["fire", 1.5]])

pokemons["charmeleon"] = pokemon("charmeleon", "fire", 60, {"headbutt": 10, "flare": 30}, [["lightning", 10]], [["water", 2]])

pokeAttack("pikachu", "charmeleon", list(pokemons["pikachu"].getStat("attacks").items())[0])
pokeAttack("charmeleon", "pikachu", list(pokemons["charmeleon"].getStat("attacks").items())[1])

print(pokemon.getPopulationHealth(pokemons))
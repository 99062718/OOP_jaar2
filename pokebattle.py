pokemons = {}

class pokemon:
    def __init__(self, name, energyType, hitpoints, attacks, resistances, weaknesses):
        self.__pokeInfo = {
            "name": name,
            "energyType": energyType,
            "hitpoints": hitpoints,
            "health": hitpoints,
            "attacks": attacks,
            "resistances": resistances,
            "weaknesses": weaknesses
        }

    def getStat(self, stat):
        return self.__pokeInfo[stat]

    def appendOrChangeStat(self, appendOrChange, statToChange, value):
        if appendOrChange == "append":
            self.__pokeInfo[statToChange].append(value)
        elif appendOrChange == "set":
            self.__pokeInfo[statToChange] = value
        elif appendOrChange == "add":
            self.__pokeInfo[statToChange] += value
        elif appendOrChange == "subtract":
            self.__pokeInfo[statToChange] -= value
        else:
            raise ValueError(f"{appendOrChange} is not a valid option for changing or adding a stat")

    def takeDamage(self, damage, energyType):
        for weakness in self.getStat("weaknesses"):
            if weakness[0] == energyType:
                damage *= weakness[1]
                break

        for resistance in self.getStat("resistances"):
            if resistance[0] == energyType:
                damage /= resistance[1]
                break

        self.appendOrChangeStat("subtract", "health", round(damage, 0))

        if self.__pokeInfo["health"] <= 0:
            self.__pokeInfo["health"] == 0
            print("{} has fainted!".format(self.getStat("name")))


def pokeAttack(nameAttacker, nameAttacked, attack):
    print(f"{nameAttacked} has {pokemons[nameAttacked].getStat('health')} hp")
    print(f"{nameAttacker} uses {attack[0]} on {nameAttacked}")
    pokemons[nameAttacked].takeDamage(attack[1], pokemons[nameAttacker].getStat("energyType"))
    print(f"{nameAttacked} has {pokemons[nameAttacked].getStat('health')} hp")

pokemons["pikachu"] = pokemon("pikachu", "lightning", 60, {"electric ring": 50, "pika punch": 20}, [["fighting", 2]], [["fire", 1.5]])

pokemons["charmeleon"] = pokemon("charmeleon", "fire", 60, {"headbutt": 10, "flare": 30}, [["lightning", 10]], [["water", 2]])

pokeAttack("pikachu", "charmeleon", list(pokemons["pikachu"].getStat("attacks").items())[0])
pokeAttack("charmeleon", "pikachu", list(pokemons["charmeleon"].getStat("attacks").items())[1])
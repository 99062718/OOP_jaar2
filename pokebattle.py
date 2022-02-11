class pokemon:
    def __init__(self, name, energyType, hitpoints, health, attacks, resistances, weaknesses):
        self.__pokeInfo = {
            "name": name,
            "energyType": energyType,
            "hitpoints": hitpoints,
            "health": health,
            "attacks": attacks,
            "resistances": resistances,
            "weakenesses": weaknesses
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
                damage /= weakness[1]
                break

        self.appendOrChangeStat("subtract", "health", round(damage, 0))

        if self.__pokeInfo["health"] <= 0:
            print("{} has fainted!".format(self.getStat("name")))
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
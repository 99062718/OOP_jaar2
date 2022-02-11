class superhero:
    def __init__(self, name, gender, team, oneliner):
        self.name = name
        self.gender = gender
        self.team = team
        self.oneliner = oneliner

    def sayOneliner(self):
        print(self.oneliner)

class avenger(superhero):
    def __init__(self, name, gender, oneliner):
        team = "Avenger"
        superhero.__init__(self, name, gender, team, oneliner)

spiderman =  superhero('Spider-Man', 'Male', 'Spiderfriends', 'With great power comes great responsibility!')
thor = avenger('Thor', 'Male', 'For Asgard!')

spiderman.sayOneliner()
thor.sayOneliner()
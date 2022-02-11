class superhero:
    def __init__(self, name, gender, team, oneliner):
        self.name = name
        self.gender = gender
        self.team = team
        self.oneliner = oneliner

    def sayOneliner(self):
        print(self.oneliner)

spiderman =  superhero('Spider-Man', 'Male', 'Spiderfriends', 'With great power comes great responsibility!')

spiderman.sayOneliner()
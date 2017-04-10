from classes.game import Person, Bcolors

magic = [{"name": "Fire", "cost": 9, "dmg": 60},
         {"name": "Thunder", "cost": 13, "dmg": 80},
         {"name": "Buzzard", "cost": 11, "dmg": 63}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0
print(Bcolors.FAIL + Bcolors.BOLD + " AN ENEMY ATTACKS" + Bcolors.ENDC)

while running:


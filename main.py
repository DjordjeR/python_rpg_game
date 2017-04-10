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
    print("==================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points. Enemy HP:", enemy.get_hp())

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacked for:", enemy_dmg, "points. You have :",
          player.get_hp(), "HP")

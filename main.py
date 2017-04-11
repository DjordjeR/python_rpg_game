from classes.game import Person, Bcolors

magic = [{"name": "Fire", "cost": 9, "dmg": 100},
         {"name": "Thunder", "cost": 13, "dmg": 124},
         {"name": "Blizzard", "cost": 11, "dmg": 110}]

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0
print(Bcolors.FAIL + Bcolors.BOLD + " AN ENEMY ATTACKS" + Bcolors.ENDC)

while running:
    print(Bcolors.HEADER + "==================" + Bcolors.ENDC)
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic spell:")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        spell_cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()
        if spell_cost > current_mp:
            print(Bcolors.FAIL + "\nNot enough MP\n" + Bcolors.ENDC)
            continue
        player.reduce_mp(spell_cost)
        enemy.take_damage(magic_dmg)
        print(Bcolors.OKBLUE + "\n" + spell + " deals", str(magic_dmg),
              "points of damage")
        print("Enemy HP:", enemy.get_hp())

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacked for:", enemy_dmg, "points.")

    print(Bcolors.HEADER + "==================" + Bcolors.ENDC)
    print("Enemy HP:", Bcolors.FAIL + str(enemy.get_hp()) + "/" +
          str(enemy.get_max_hp()) + Bcolors.ENDC + "\n")

    print("Your HP:", Bcolors.OKGREEN + str(player.get_hp()) + "/" +
          str(player.get_max_hp()) + Bcolors.ENDC)
    print("Your MP:", Bcolors.OKBLUE + str(player.get_mp()) + "/" +
          str(player.get_max_mp()) + Bcolors.ENDC + "\n")

    if enemy.get_hp() == 0:
        print(Bcolors.OKGREEN + "You win!" + Bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Bcolors.FAIL + "Your enemy has defeated you!" + Bcolors.ENDC)
        running = False
import random


class Bcolors:  # class for terminal colors
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:  # Person class
    # Constructor
    def __init__(self, hp, mp, atk, df, magic, items):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.action = ["Attack", "Magic", "Items"]

    # Getters
    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    # Randomly generate damage output, interval from attack low to attack high
    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    # Subtract taken damage from current health status
    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:  # We do not want hp to be less then 0
            self.hp = 0
        return self.hp

    # Ability to get some health back
    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    # Reduce magic points when using magic
    def reduce_mp(self, cost):
        self.mp -= cost

    # Print out options for choosing action
    def choose_action(self):
        print("\n" + Bcolors.OKGREEN + Bcolors.BOLD + "ACTIONS:" + Bcolors.ENDC)
        i = 1
        for item in self.action:
            print("    " + str(i) + ".", item)
            i += 1

    # Print out options for choosing magic
    def choose_magic(self):
        print("\n" + Bcolors.OKGREEN + Bcolors.BOLD + "MAGIC:" + Bcolors.ENDC)
        i = 1
        for spell in self.magic:
            print("    " + str(i) + ".", spell.name, "(cost :", str(spell.cost)
                  + ")")
            i += 1

    # Print out item options
    def choose_items(self):
        i = 1;
        print("\n" + Bcolors.OKGREEN + Bcolors.BOLD + "ITEMS:" + Bcolors.ENDC)
        for item in self.items:
            print("    " + str(i) + ".", item.name, ":", item.description, "5")
            i += 1
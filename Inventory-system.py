class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.inventory = []


    def add(self, item):
            self.inventory.append(item)

    def display_inventory(self):
        displayDict = {}

        for item in self.inventory:
            if item.name not in displayDict:
                displayDict[item.name] = 0

            displayDict[item.name] += 1

        for name, quantity in displayDict.items():
            print(f"{name} × {quantity}")


    def view_stats(self):
        x = 8
        print(f'{"=" * x}| {self.name.capitalize()} |{"=" * x}')
        print(f'{" " * int(x / 2)}health: {self.health}')
        print("\n")
        print("\n")
        print(f'{"=" * x}| Inventory |{"=" * x}')
        self.display_inventory()

    def use_item(self, item):
        if item in self.inventory:
            item.use_item(self)
        if item.consumable == True:
            self.inventory.remove(item)

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value


class Weapon(Item):
    def __init__(self, name, weight, value, damage):
        super().__init__(name, weight, value)
        self.damage = damage
        self.consumable = False


    def use_item(self, item):
        print(f"{item.name} attacked")

class Potion(Item):
    def __init__(self, name, weight, value, heal_amount):
        super().__init__(name, weight, value)
        self.heal_amount = heal_amount


    def use_item(self, user):
        user.health += self.heal_amount
        print(f"{self.name.capitalize()} restored {self.heal_amount} HP points")

class Shield(Item):
    def __init__(self, name, weight, value, defense):
        super().__init__(name, weight, value)
        self.defense = defense
        self.consumable = False

    slot_full = False
    def use_item(self):
        if self.slot_full == False:
            print(f"{self.name} was equipped")
            self.slot_full = True
        if self.slot_full == True:
            print("Slot full, please unequipp current Shield")

    def unequipp(self, item):
        self.slot_full = False
        print(f"Unequipped {item.name}")

sword = Weapon("Iron Sword", 5, 50, 20)
potion = Potion("Health Potion", 1, 15, 30)
shield = Shield("Wooden Shield", 8, 35, 10)
sword = Weapon("Iron Sword", 8, 30, 50)
print(sword.damage)
print(sword.value)
print(potion.heal_amount)

cooldude = Character("cool_kid", 100)
cooldude.add(potion)
cooldude.add(potion)
cooldude.add(potion)
cooldude.add(sword)
cooldude.add(sword)
cooldude.display_inventory()
cooldude.use_item(sword)
cooldude.display_inventory()
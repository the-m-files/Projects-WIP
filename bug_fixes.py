
import random


class Creature:
    def __init__(self, name, health=100, energy=50, strength=10):
        self.name = name
        self.health = health
        self.energy = energy
        self.strength = strength

    def train(self): 
        """
        Whenever this function is called, it subtracts 10 units from energy, and adds 5 to stregnth. If its lower than 10 then it avoids it.
         """
        if self.energy >= 10:
            self.strength += 5
            self.energy -= 10
            print(f"{self.name} trained! Strength: {self.strength}")
        else:
            print(f"{self.name} is too tired to train!")

    def rest(self):
        """
        Whenever this function is called, it adds 20 units to energy, if energy is more than 100, then it sets it to a 100 if this function is called.
        """
        self.energy += 20
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} rested. Energy: {self.energy}")

    def eat(self):
        """
        This just increases the health by 15 units no matter what.
        """
        self.health += 15
        print(f"{self.name} ate. Health: {self.health}")

    def attack(self, opponent):
        """
        If the energy of the attacking mob is greater than 0, then it will subtract the opponents health by its stregnth, else it avoids it.
        """
        if self.energy > 0:
            opponent.health -= self.strength
            self.energy -= 10
            print(f"{self.name} attacked {opponent.name}!")
        else:
            print(f"{self.name} is too tired to attack!")

    def is_alive(self):
        """
        This method says whether the health of a mob is greater than 0
        """
        return self.health > 0

    def status(self):
        """
        This basically spits out all the attributes of the mob, like __repr__ but customized and inneficient.
        """
        print(
            f"{self.name}: HP={self.health}, "
            f"Energy={self.energy}, Strength={self.strength}"
        )


def battle(creature1, creature2): #this function doesn't have any bugs atleast according to me.
    """
    Simulates a battle by attacking eachother.
    """
    turn = 0

    while creature1.is_alive() and creature2.is_alive():
        turn += 1
        print(f"\n--- Turn {turn} ---")

        if turn % 2 == 1: #whenever turn is odd, the creature1 attacks.
            creature1.attack(creature2)
        else:
            creature2.attack(creature1)

        if turn > 20:
            print("Battle timed out!")
            break

    print("\nBattle over!")
    creature1.status()
    creature2.status()


# Test arena
slime = Creature("Slime", health=40, energy=30, strength=10)
dragon = Creature("Dragon", health=60, energy=20, strength=20)

# slime.status()
# slime.train() #train works
# slime.status()

slime.status()
slime.rest()
slime.status()
print("\n=== BATTLE ===")
battle(slime, dragon)

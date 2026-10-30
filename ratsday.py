import time
import random
Rat_Population = []
print("========== NEW VERSION ==========")
print("RUNNING CURRENT FILE")
class Rat:
    def __init__(self, name, mood, heal_factor):
        self.name = name
        self.hunger = 10  #80-100 means heal 20-35 means starve and lose health. hunger can be atmost 100
        self._health = 10
        self.food_nearby = 3
        #mood at max(100 or whatever they choose will call a random method) every second it increases by 1
        self.mood = mood #this determines if they are motivated enough to do something(call a method), slowly increases by time
        self.heal_factor = heal_factor
        self.feeling = ["Greedy", "Curious", "Hungry"]
        self.personality = random.choice(self.feeling)
        print(self.personality)
        Rat_Population.append(self)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        elif value > 100:
            self._health = 100
        else:
            self._health = value
                
    #considering mood is high enough:
    def act(self):
        if self.personality == "Hungry":
            self.eat()

        elif self.personality == "Curious":
            self.wander()

        elif self.personality == "Greedy":
            possible_targets = [rat for rat in Rat_Population if rat != self]

            if possible_targets:
                target = random.choice(possible_targets)

                print(f"{self.name} is trying to steal from {target.name}")

                self.steal(target)
        self.mood = 0
    def eat(self):
        if self.food_nearby > 0 and self.hunger < 100:
            self.food_nearby -= 1
            self.hunger += self.food_nearby*self.heal_factor
            
            if self.health+self.food_nearby*self.heal_factor > 100:
                self.health = 100
            else:
                self.health += self.heal_factor*self.food_nearby
                print(f"{self.name} ate and healed {self.heal_factor*self.food_nearby}")
                print(f"{self.name}'s health is now {self.health}")         
                print(f"{self.name} now feels {self.personality}")
        else:
            print("Insufficient state to eat")

    def wander(self):
        distance = 10 #this is supposed to be random and lower the hunger value but also increase the chance of getting food_nearby up
        if self.hunger - round(distance/2) < 0:
            return self.die()
        else:
            self.hunger -= round(distance/2)
            print(f"{self.name} wandered {distance} and lost {round(distance/2)} hunger")
            self.food_nearby += round(distance/2.5) + self.heal_factor

    def steal(self, target):
        if target.food_nearby - self.heal_factor*2 <= 0:
            self.food_nearby += target.food_nearby
            target.food_nearby = 0
        else:
            stolen_food = self.heal_factor*2
            self.food_nearby += stolen_food
            target.food_nearby -= stolen_food

    def die(self):
        if self.hunger <= 0:
            print(f"{self.name} died")
            Rat_Population.remove(self)

    def display(self):
        print(f"------ {self.name.capitalize()} ------")
        print(f"Health:       {self._health}")
        print(f"Mood:         {self.mood}")
        print(f"Hunger:       {self.hunger}")
        print(f"Food Nearby:  {self.food_nearby}")
        print(f"Feeling:      {self.personality}")
        print(f"{6*"-"}Actions{6*"-"}")
        self.debug()
        #print("\n")
    
    def debug(self):

        if self.food_nearby < 0:
            print(f"BUG: {self.name} has negative food: {self.food_nearby}")

        if self.hunger < 0:
            print(f"BUG: {self.name} has negative hunger: {self.hunger}")

        if self.hunger > 100:
            print(f"BUG: {self.name} has hunger over 100: {self.hunger}")

        if self.health < 0:
            print(f"BUG: {self.name} has negative health: {self.health}")

        if self.health > 100:
            print(f"BUG: {self.name} has health over 100: {self.health}")

    def __repr__(self):
        return self.name

rat1 = Rat("Mongo", 3, 2)
rat2 = Rat("Chucky", 10, 5)

print(Rat_Population)

second = 0

while len(Rat_Population) != 0:
    if __name__ == "__main__":
        rat1 = Rat("Mongo", 3, 2)
        rat2 = Rat("Chucky", 10, 5)

        print(Rat_Population)

        while len(Rat_Population) != 0:
            for rat in Rat_Population.copy():

                rat.mood += 1

                if rat.mood > 5:
                    rat.act()
                    rat.display()

                rat.die()

            time.sleep(1)
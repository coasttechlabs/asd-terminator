import battle_bot
import random

def handle_imput(self, level):
    choice = handle_imput( "choose (h)eal or (r)echarge or (l)eave or (a)ttack or (d)efend: ")
    if choice == "h":
        self.heal_health
    elif choice == "r":
        self.recharge_battery(level) # level affects recharge
    elif choice == "l":
        self.leave
    elif choice == "a":
          self.do_attack(level) # level affects attack
    elif choice == "d":
          self.do_defend(level) # level affects defend
       

def heal_health(self):
        print(f"{self.name} are healing!")
        heal_amount = random.randint(1, 10)
        self.current_health += heal_amount
        print( f"{self.name} healed {heal_amount} health!")
        player_battery_used = random.randint(1, 10)
        player_battery_used -= self.battery_life
        print(f"{self.name} used {player_battery_used}")

def recharge_battery(self):
        print(f"{self.name} is recharging!")
        recharge_amount = random.randint(1, 10)
        self.battery_life += recharge_amount
        print( f"{self.name} recharged {recharge_amount} battery!")

def leave(self):
        print(f"{self.name} is running away")
        #then they would leave combat

def do_attack(self):
      print(f"{self.name} is attacking {self.enemy_name}!")
      player_attack_amount = random.randint(1, 10)
      self.enemy_health -= player_attack_amount
      print(f"{self.name} dealt {player_attack_amount} to {self.enemy_name} ")
      player_battery_used = random.randint(1, 10)
      player_battery_used -= self.battery_life
      print(f"{self.name} used {player_battery_used}")

def do_defend(self):
      print(f"{self.name} is goind to defend against {self.enemy_name}!")
      player_defend_amount = random.ranint(1, 10)
      self.enemy_attack_amount -= player_defend_amount
      player_battery_used = random.randint(1, 10)
      player_battery_used -= self.battery_life
      print(f"{self.name} used {player_battery_used}")

def desert_level(self, level):
        if level ["name"] == "desert":
            self.battery_life += 10  # Recharge battery in desert
            print(f"☀️ {self.name} is benefiting from the desert heat!")

def forest_level(self, level):
        if level ["name"] == "forest":
            self.defense += 5  # Increase defense in forest
            print(f"🌳 {self.name} is using the trees for cover, increasing defense!")

def frozen_lake_level(self, level):
        if level ["name"] == "frozen lake":
            self.dodge_chance += 15  # Increase dodge chance on frozen lake
            print(f"❄️ {self.name} is slipping around on the frozen lake, increasing dodge chance!")
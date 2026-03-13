import random
import time
from commentary import get_commentary

class BattleBot:
    def __init__(self, name):
        self.name = name
        self.max_health = 100
        self.current_health = 100
        self.strength = random.randint(10, 20)  
        self.defense = random.randint(0, 5)     
        self.battery_life = random.randint(50, 100) 
        self.dodge_chance = random.randint(10, 25)
        # print(f"🤖 FACTORY: Built {self.name} | STR: {self.strength} | DEF: {self.defense} | BATT: {self.battery_life}% | DODGE: {self.dodge_chance}%")

    # def heal(self, amount):
    #     self.current_health = min(self.max_health, self.current_health + amount)
    #     print(f"   💊 {self.name} healed for {amount} health!")
    #     print(f"   ❤️ Health: {self.current_health}/{self.max_health}")
    #     print(get_commentary("heal", self.name))

    # def recharge(self, amount):
    #     self.battery_life = min(100, self.battery_life + amount)
    #     print(f"   ⚡ {self.name} recharged by {amount}%. Current Battery: {self.battery_life}%")
    #     print(get_commentary("recharge", self.name))

    # def battery_drain(self, amount):
    #     self.battery_life = max(0, self.battery_life - amount)
    #     print(f"   🔋 {self.name}'s battery drained by {amount}%. Remaining: {self.battery_life}%")

    def attack(self, enemy, round_num):
        print(f"\n⚔️ {self.name} attacks {enemy.name}!")
        time.sleep(1)
        if random.randint(1,100) <= enemy.dodge_chance:
            print(f"  💨SWOOSH! {enemy.name} swiftly doged the attack!")
            print(get_commentary("dodge", enemy.name))
            return

        damage = self.strength - enemy.defense

        if round_num >= 5 and random.randint(1, 100) > 50:
            damage = int(damage * 1.5)
            print(" ⚠️ LATE ROUND SURGE! Damage increased by 50%! ⚠️")
        
    #     if random.randint(1, 100) > 80:
    #         damage = damage * 2
    #         print("   🔥 CRITICAL HIT! Double Damage! 🔥")
    #         print(get_commentary("crit"))

    #     damage = max(0, damage)
    #     enemy.take_damage(damage)

    # def take_damage(self, amount):
    #     self.current_health -= amount
    #     print(f"   💥 {self.name} took {amount} damage!")
    #     print(f"   ❤️ Health: {self.current_health}/{self.max_health}")

    # def is_alive(self):
    #     return self.current_health > 0
    
    def take_turn(self, enemy, round_num):
        """Encapsulates the logic for a single bot's turn."""
        if not self.is_alive():
            return
            
        if self.battery_life > 0:
            self.battery_drain(random.randint(5, 25))
            self.attack(enemy, round_num)
        else:
            print(f"⚠️ {self.name} has no battery left and cannot attack! Enacting emergency recharge...")
            print(get_commentary("battery_dead", self.name))
            self.recharge(random.randint(20, 40))

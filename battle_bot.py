import random
import time
from commentary import get_commentary
from weapons import Weapon 

class BattleBot:
    def __init__(self, name):
        self.name = name
        self.max_health = 100
        self.current_health = 100
        self.strength = random.randint(10, 20)  
        self.defense = random.randint(0, 5)     
        self.battery_life = random.randint(50, 100) 
        self.dodge_chance = random.randint(10, 25)
        
        # Weapon Instance
        available_choices = ["Decimator", "Cain-Sword", "plasma-gun", "rifle"]
        self.weapon = Weapon(random.choice(available_choices))
        
        print(f"🤖 FACTORY: {self.name} online.")
        print(f"📦 LOADOUT: {self.weapon.category} - {self.weapon.weapon_name} (+{self.weapon.strength_bonus} DMG)")

    def heal(self, amount):
        """Standard heal method called by main.py or internal logic."""
        self.current_health = min(self.max_health, self.current_health + amount)
        print(f"   💊 {self.name} performed repairs! +{amount} HP.")
        print(f"   ❤️ Health: {self.current_health}/{self.max_health}")
        print(get_commentary("heal", self.name))

    def attack(self, enemy, round_num):
        print(f"\n⚔️ {self.name} strikes {enemy.name} with {self.weapon.weapon_name}!")
        
        if random.randint(1, 100) <= enemy.dodge_chance:
            print(f"  💨 {enemy.name} dodged the {self.weapon.weapon_name}!")
            return

        total_power = self.strength + self.weapon.strength_bonus
        damage = total_power - enemy.defense

        if random.random() > 0.7:
            print(f"  ✨ EFFECT: {self.weapon.apply_effects()}")

        if round_num >= 5:
            damage = int(damage * 1.5)
        
        damage = max(2, damage) 
        enemy.take_damage(damage)

    def take_damage(self, amount):
        self.current_health -= amount
        print(f"   💥 {self.name} took {amount} damage! (HP: {self.current_health})")

    def is_alive(self):
        return self.current_health > 0

    def take_turn(self, enemy, round_num):
        if not self.is_alive():
            return

        # NEW: Emergency Self-Repair Logic
        # If health is below 30%, there's a 30% chance to heal instead of attacking
        if self.current_health < 30 and random.random() < 0.3:
            self.heal(random.randint(15, 25))
            return 

        if self.battery_life > 0:
            self.battery_life -= random.randint(5, 15)
            self.attack(enemy, round_num)
        else:
            print(f"🪫 {self.name} is recharging...")
            self.battery_life += 30
            self.heal(5) # Small passive heal during recharge
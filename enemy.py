import random
import battle_bot

def __init__(self, name, enemy, health, strength, defense, attack):
        self.name = name
        self.enemy = enemy
        self.current_health = health
        self.strength = strength 
        self.defense = defense
        self.attack = attack

def enemy_name(self, enemy):
        if self.enemy_name == "wall-e":
            return self.enemy 

def enemy_turn(self, enemy):
    if self.enemy.is_alive():
        self.enemy.take_turn(self)
    if self.enemy.current_health < 25:
        self.enemy.heal(random.randint(10, 20))
    if self.enemy.current_health > 25:
        self.enemy.attack(self)

def attack (self, enemy):
        enemy_attack_amount = random.randint(1, 10) 

def defend (self, enemy):
        enemy_defend_amount = random.randint(1, 10)

def health (self):
        enemy_health_amount = random.randint(1, 10)
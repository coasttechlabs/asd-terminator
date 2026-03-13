import battle_bot

class weapons:
    def __init__(self, name, weapon, weapon_effects,):
        self.name = name
        self.weapon_effects = weapon_effects
        self.weapon = weapon
        self.weapon_name = weapon
        self.weapon_strength = weapon_effects
    
    def get_weapon_info(self):
        return f"{self.name} wields a {self.weapon_name} with effects {self.weapon_effects}."
    
    def get_weapon_info(self):
        print(f"{self.name} wields a {self.weapon_name}.")

    def weapon_type(self):
        if self.weapon_strength >= 15:
            return "Heavy Weapon"
        elif self.weapon_strength >= 10:
            return "Medium Weapon"
        else: 
            return "Light Weapon"
        
    def weapon_names(self, weapon):
        if self.weapon == "Decimator":
            return "Decimator"
        elif self.weapon == "Cain-Sword":
            return "Cain-Sword"
        elif self.weapon == "plasma-gun":
            return "plasma-gun"
        else:
            return self.weapon
    
    def weapon_statistics(self, weapon):
        if self.weapon == "Decimator":
            return {"name": "Decimator", "strength": 20, "type": "Heavy Blade, explosive, melee"}
        elif self.weapon == "Cain-Sword":
            return {"name": "Cain-Sword", "strength": 5, "type": "Light Blade, multiple strikes, melee"}
        elif self.weapon == "plasma-gun":
            return {"name": "plasma-gun", "strength": 10, "type": "Ranged, overheat"}
        else:
            return {"name": self.weapon, "strength": 0, "type": "Unknown"}
        
    def weapon_effects(self, weapon_effects):
            self.explosive_effects = ["Area damage"]
            self.multiple_strikes_effects = ["hits multiple times in one turn"]
            self.deadly_demise_effects = ["random randint(1, 100) rolls a 1-10 self damage"]
            self.melee_effects = ["close proximity to deal damage"]
            self.ranged_effects = ["can attack from a distance"]
            self.over_heat_effects = ["adds 5 weapon strength but deadly demise effect applies"]

    def apply_weapon_effects(self, enemy):
        if self.weapon_effects == "explosive":
            return f"{self.explosive_effects}!"
        if self.weapon_effects == "multiple strikes":
            return f"{self.multiple_strikes_effects}!"
        if self.weapon_effects == "deadly demise":
            return f"{self.deadly_demise_effects}!"
        if self.weapon_effects == "melee":
            return f"{self.melee_effects}!"
        if self.weapon_effects == "ranged":
            return f"{self.ranged_effects}!"
        if self.weapon_effects == "overheat":
            return f"{self.over_heat_effects}!"
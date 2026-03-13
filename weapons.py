import random

class Weapon: # Renamed to singular 'Weapon' for PEP8 standards
    def __init__(self, weapon_name):
        self.weapon_name = weapon_name
        # Fetch stats immediately upon initialization
        stats = self.get_weapon_statistics(weapon_name)
        self.strength_bonus = stats["strength"]
        self.type_description = stats["type"]
        self.category = self.determine_category()

    def determine_category(self):
        if self.strength_bonus >= 15:
            return "Heavy Weapon"
        elif self.strength_bonus >= 10:
            return "Medium Weapon"
        else: 
            return "Light Weapon"
        
    def get_weapon_statistics(self, name):
        # Database of weapon stats
        weapons_data = {
            "Decimator": {"strength": 20, "type": "Heavy Blade, explosive, melee"},
            "Cain-Sword": {"strength": 5, "type": "Light Blade, multiple strikes, melee"},
            "plasma-gun": {"strength": 12, "type": "Ranged, overheat"},
            "rifle": {"strength": 10, "type": "hybrid"}
        }
        return weapons_data.get(name, {"strength": 5, "type": "Unknown"})

    def apply_effects(self):
        """Returns a string description of the weapon's special trait."""
        if "explosive" in self.type_description:
            return "💥 Area damage potential!"
        if "multiple strikes" in self.type_description:
            return "⚔️ Rapid fire strikes!"
        if "overheat" in self.type_description:
            return "🔥 High heat, high damage!"
        return "🛡️ Standard combat mode."
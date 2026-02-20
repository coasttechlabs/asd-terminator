import random
import time
import meme_generator

# --- NEW: LIVE COMMENTARY DICTIONARY ---
COMMENTARY = {
    "round_start": [
        "🎙️ COMMENTATOR: The gears are grinding! Let's see what happens this round.",
        "🎙️ COMMENTATOR: Both combatants are looking for an opening...",
        "🎙️ COMMENTATOR: I can smell the burning ozone from here! Here we go!",
        "🎙️ COMMENTATOR: Will this be the round that changes everything?"
    ],
    "crit": [
        "🎙️ COMMENTATOR: OH THE HUMANITY! Er, ROBOT-ITY! What a massive critical hit!",
        "🎙️ COMMENTATOR: Right in the CPU! That's going to void the warranty!",
        "🎙️ COMMENTATOR: BAH GAWD! He's broken in half! Sparks are flying everywhere!"
    ],
    "heal": [
        "🎙️ COMMENTATOR: Looks like {bot} is applying some tactical duct tape!",
        "🎙️ COMMENTATOR: A quick self-repair protocol for {bot}. They're back in the fight!",
        "🎙️ COMMENTATOR: {bot} is patching up those dents. Smart strategy!"
    ],
    "battery_dead": [
        "🎙️ COMMENTATOR: Oh no! {bot} is completely out of juice! They're a sitting duck!",
        "🎙️ COMMENTATOR: Someone get {bot} a charging cable, STAT!"
    ],
    "recharge": [
        "🎙️ COMMENTATOR: {bot} is desperately siphoning power from the arena floor!",
        "🎙️ COMMENTATOR: Emergency power engaged for {bot}!"
    ],
    "win": [
        "🎙️ COMMENTATOR: AND IT'S ALL OVER! {bot} takes the scrap-metal crown!",
        "🎙️ COMMENTATOR: What an unbelievable match! {bot} proves to be the ultimate machine today!"
    ]
}

def get_commentary(event_type, bot_name=""):
    """Fetches a random commentary line based on the event."""
    phrases = COMMENTARY.get(event_type, ["🎙️ COMMENTATOR: ..."])
    chosen_phrase = random.choice(phrases)
    return chosen_phrase.format(bot=bot_name)


# --- TICKET #2: DESIGN THE BLUEPRINT ---
class BattleBot:
    def __init__(self, name):
        self.name = name
        self.max_health = 100
        self.current_health = 100
        self.strength = random.randint(10, 20)  # RNG Strength
        self.defense = random.randint(0, 5)     # RNG Defense
        self.battery_life = random.randint(50, 100)  # New Attribute for Future Expansion
        print(f"🤖 FACTORY: Built {self.name} | STR: {self.strength} | DEF: {self.defense}")

    # --- TICKET #10: Add Health to BattleBot ---
    def heal(self, amount):
        self.current_health = min(self.max_health, self.current_health + amount)
        print(f"   💊 {self.name} healed for {amount} health!")
        print(f"   ❤️ Health: {self.current_health}/{self.max_health}")

    def recharge(self, amount):
        self.battery_life = min(100, self.battery_life + amount)
        print(f"   ⚡ {self.name} recharged by {amount}%. Current Battery: {self.battery_life}%")

    def battery_drain(self, amount):
        self.battery_life = max(0, self.battery_life - amount)
        print(f"   🔋 {self.name}'s battery drained by {amount}%. Remaining: {self.battery_life}%")


    # --- TICKET #3: COMBAT LOGIC ---
    def attack(self, enemy):
        print(f"\n⚔️ {self.name} attacks {enemy.name}!")
        time.sleep(1) # Suspense

        # Calculate Damage
        damage = self.strength - enemy.defense
        
        # Critical Hit Logic (20% chance)
        if random.randint(1, 100) > 80:
            damage = damage * 2
            print("   🔥 CRITICAL HIT! Double Damage! 🔥")

        # Prevent negative damage (healing the enemy)
        damage = max(0, damage)

        # Apply the hit
        enemy.take_damage(damage)

    def take_damage(self, amount):
        self.current_health -= amount
        print(f"   💥 {self.name} took {amount} damage!")
        print(f"   ❤️ Health: {self.current_health}/{self.max_health}")

    def is_alive(self):
        return self.current_health > 0

# --- TICKET #4: THE BATTLE LOOP ---
if __name__ == "__main__":
    print("📢 WELCOME TO THE INNOVATION CENTRE FIGHT CLUB 📢")
    
    # Spawn the Fighters
    bot1 = BattleBot("Terminators")
    bot2 = BattleBot("Wall-E")

    round_num = 1

    # Fight until one dies
    while bot1.is_alive() and bot2.is_alive():
        print(f"\n--- ROUND {round_num} --- ")
        if bot1.battery_life > 0:
            print(f"   🔋 {bot1.name}'s battery drained by {random.randint(5, 25)}%. Remaining: {bot1.battery_life}%")
            bot1.battery_drain(random.randint(5, 25))
        if bot2.battery_life > 0:
            print(f"   🔋 {bot2.name}'s battery drained by {random.randint(5, 25)}%. Remaining: {bot2.battery_life}%")
            bot2.battery_drain(random.randint(5, 25))

        if bot1.battery_life == 0:
            print(f"⚠️ {bot1.name} has no battery left and cannot attack! inacting emergency recharge protocol...")
            bot1.recharge(random.randint(20, 40))

        if bot2.battery_life == 0:
            print(f"⚠️ {bot2.name} has no battery left and cannot attack! inacting emergency recharge protocol...")
         
        if round_num % 3 == 0:  # Every 3 rounds, both bots heal
            bot1.heal(random.randint(10, 20))
            bot2.heal(random.randint(10, 20))

        if bot1.battery_life > 0:
            bot1.attack(bot2)
        
        # Check if bot2 survived befoSre counter-attacking
        if bot2.is_alive() and bot2.battery_life > 0:
            bot2.attack(bot1)

        round_num += 1
        time.sleep(1.5)

    print("\n🏆 GAME OVER 🏆")
    if bot1.is_alive():
        print(f"🎉 {bot1.name} WINS!")
        meme_generator.generate_terminator_meme(bot1.name) # <--- Trigger Meme
    else:
        print(f"🎉 {bot2.name} WINS!")
        meme_generator.generate_terminator_meme(bot2.name) # <--- Trigger Meme

import random

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
    ],
    # NEW: Dodge commentary lines
    "dodge": [
        "🎙️ COMMENTATOR: Wow! {bot} moved with the speed of a greased microchip!",
        "🎙️ COMMENTATOR: A clean miss! {bot} dances right around that attack!",
        "🎙️ COMMENTATOR: Whoa! Is {bot} programmed with the Matrix dodge module?!",
        "🎙️ COMMENTATOR: Whiff! They're punching air out there!"
    ]
}

def get_commentary(event_type, bot_name=""):
    """Fetches a random commentary line based on the event."""
    phrases = COMMENTARY.get(event_type, ["🎙️ COMMENTATOR: ..."])
    chosen_phrase = random.choice(phrases)
    return chosen_phrase.format(bot=bot_name)
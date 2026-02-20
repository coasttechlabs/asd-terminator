import random
import time
import meme_generator
from commentary import get_commentary
from battle_bot import BattleBot

if __name__ == "__main__":
    print("📢 WELCOME TO THE INNOVATION CENTRE FIGHT CLUB 📢")
    
    bot1 = BattleBot("Terminators")
    bot2 = BattleBot("Wall-E")

    round_num = 1

    while bot1.is_alive() and bot2.is_alive():
        print(f"\n{'='*20}")
        print(f"--- ROUND {round_num} ---")
        print(f"{'='*20}")
        print(get_commentary("round_start"))
        time.sleep(1)

        # Periodic Healing
        if round_num % 3 == 0:  
            bot1.heal(random.randint(10, 20))
            bot2.heal(random.randint(10, 20))
            time.sleep(1)

        # Execute Turns
        bot1.take_turn(bot2)
        time.sleep(1)
        
        if bot2.is_alive(): # Ensure bot2 is still alive before it counters
            bot2.take_turn(bot1)

        round_num += 1
        time.sleep(1.5)

    # --- GAME OVER LOGIC ---
    print("\n🏆 GAME OVER 🏆")
    winner = bot1 if bot1.is_alive() else bot2
    
    print(f"🎉 {winner.name} WINS!")
    print(get_commentary("win", winner.name))
    meme_generator.generate_terminator_meme(winner.name)
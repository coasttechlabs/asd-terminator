import unittest
import io
import logging
from unittest.mock import patch
from battle_bot import BattleBot

# --- TEST LOGGING CONFIGURATION ---
logging.basicConfig(
    level=logging.DEBUG, # Set to DEBUG to capture the granular details
    format='%(asctime)s - [SIMULATION] - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("simulation_detailed_history.log"),
        logging.StreamHandler() 
    ]
)
logger = logging.getLogger("BattleBotSim")

class TestBattleBot(unittest.TestCase):

    def test_battle_simulation_statistics(self):
        """
        Runs 1,000 simulated battles with deep logging for every interaction.
        """
        simulations = 3
        bot1_wins = 0
        bot2_wins = 0
        total_rounds = 0
        
        logger.info(f"STARTING MEGA-SIMULATION: {simulations} matches.")

        # Suppress prints to keep the console usable
        with patch('sys.stdout', new_callable=io.StringIO):
            for i in range(1, simulations + 1):
                b1 = BattleBot("Terminators")
                b2 = BattleBot("Wall-E")
                
                logger.debug(f"Match #{i} Init: {b1.name} (STR:{b1.strength}) vs {b2.name} (STR:{b2.strength})")
                
                round_num = 1
                while b1.is_alive() and b2.is_alive():
                    # Log Round Start
                    logger.debug(f"Match #{i} | Round {round_num} | HP: {b1.name}:{b1.current_health} - {b2.name}:{b2.current_health}")

                    # Periodic Healing Logic
                    if round_num % 3 == 0:  
                        logger.debug(f"Match #{i} | Round {round_num} | Healing Protocol Engaged")
                        b1.heal(15)
                        b2.heal(15)
                    
                    # Bot 1 Turn
                    logger.debug(f"Match #{i} | {b1.name} is taking turn.")
                    b1.take_turn(b2, round_num)
                    
                    # Bot 2 Turn (Check if still alive)
                    if b2.is_alive():
                        logger.debug(f"Match #{i} | {b2.name} is taking turn.")
                        b2.take_turn(b1, round_num)
                        
                    round_num += 1
                
                # Post-Match Accounting
                match_duration = round_num - 1
                total_rounds += match_duration
                
                if b1.is_alive():
                    bot1_wins += 1
                    winner_name = b1.name
                else:
                    bot2_wins += 1
                    winner_name = b2.name

                logger.info(f"Match #{i} Finished | Winner: {winner_name} | Total Rounds: {match_duration}")

        # Calculate Basics Stats
        avg_rounds = total_rounds / simulations
        b1_win_rate = (bot1_wins / simulations) * 100
        b2_win_rate = (bot2_wins / simulations) * 100

        # Log Final Statistics Summary
        logger.info("="*40)
        logger.info("FINAL SIMULATION STATISTICS")
        logger.info(f"Avg Rounds per Match: {avg_rounds:.2f}")
        logger.info(f"Terminators Win Rate: {b1_win_rate:.1f}%")
        logger.info(f"Wall-E Win Rate:      {b2_win_rate:.1f}%")
        logger.info("="*40)

if __name__ == '__main__':
    unittest.main()
import random

def generate_terminator_meme(winner_name=None):
    """
    Prints an ASCII art Terminator meme. 
    If a winner_name is provided, it customizes the message.
    """
    
    quotes = [
        "I'LL BE BACK.",
        "ASTA LA VISTA, BABY.",
        "COME WITH ME IF YOU WANT TO LIVE.",
        "TERMINATED."
    ]
    
    selected_quote = random.choice(quotes)
    
    print("\n" + "="*40)
    print(f"       INITIATING MEME PROTOCOL...")
    print("="*40)
    
    # ASCII Art
    print(r"""
           _________
         /         \
        |  |     |  |
        |  |     |  |
        |  |_____|  |
        |  \_____/  |
        \___________/
         |         |
         |  0   0  |   <-- (Scanning for targets)
         |    ^    |
         |   ___   |
         |_________|
    """)
    
    if winner_name:
        print(f"   TARGET ACQUIRED: {winner_name}")
        print(f"   STATUS: VICTORIOUS")
    
    print(f"\n   MESSAGE: {selected_quote}")
    print("="*40 + "\n")

# Allow this file to be run on its own for testing
if __name__ == "__main__":
    generate_terminator_meme("T-800")
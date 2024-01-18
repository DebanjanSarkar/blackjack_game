import random

blackjack_title = """
                                 _____
     _____                _____ |6    |
    |2    | _____        |5    || v v |
    |  v  ||3    | _____ | v v || v v | _____
    |     || v v ||4    ||  v  || v v ||7    |
    |  v  ||     || v v || v v ||____9|| v v | _____
    |____Z||  v  ||     ||____S|       |v v v||8    | _____
           |____E|| v v |              | v v ||v v v||9    |
                  |____h|              |____L|| v v ||v v v|
                                              |v v v||v v v|
                                              |____8||v v v|
                                                     |____6|
         _     _            _    _            _    
        | |   | |          | |  (_)          | |   
        | |__ | | __ _  ___| | ___  __ _  ___| | __
        | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        | |_) | | (_| | (__|   <| | (_| | (__|   < 
        |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                            _/ |                
                            |__/               
_____________________________________________________________
"""

win_ascii_art = """
 __     __           __          _______ _   _ _ 
 \ \   / /           \ \        / /_   _| \ | | |
  \ \_/ /__  _   _    \ \  /\  / /  | | |  \| | |
   \   / _ \| | | |    \ \/  \/ /   | | | . ` | |
    | | (_) | |_| |     \  /\  /   _| |_| |\  |_|
    |_|\___/ \__,_|      \/  \/   |_____|_| \_(_)
                                                
-------------------------------------------------------
"""

lose_ascii_art = """
 __     __            _      ____   _____ ______ _ 
 \ \   / /           | |    / __ \ / ____|  ____| |
  \ \_/ /__  _   _   | |   | |  | | (___ | |__  | |
   \   / _ \| | | |  | |   | |  | |\___ \|  __| | |
    | | (_) | |_| |  | |___| |__| |____) | |____|_|
    |_|\___/ \__,_|  |______\____/|_____/|______(_)
                                                  
-------------------------------------------------------
"""

tie_ascii_art = """
  _____  _                   _______  _____  ______  _ 
 |_   _|| |                 |__   __||_   _||  ____|| |
   | |  | |_  ___     __ _     | |     | |  | |__   | |
   | |  | __|/ __|   / _` |    | |     | |  |  __|  | |
  _| |_ | |_ \__ \  | (_| |    | |    _| |_ | |____ |_|
 |_____| \__||___/   \__,_|    |_|   |_____||______|(_)
                                                       
--------------------------------------------------------
"""

card_names = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "king", "queen", "jack"]
card_values = {
    "ace": 11, 
    "2": 2, 
    "3": 3, 
    "4": 4, 
    "5": 5, 
    "6": 6, 
    "7": 7, 
    "8": 8, 
    "9": 9, 
    "10": 10, 
    "king": 10, 
    "queen": 10, 
    "jack": 10,
}



def get_random_card():
    """Returns the name of a random card among the possible/available cards."""

    return random.choice(card_names)



def get_card_value(card_name):
    """Takes the card name as parameter, whose value is to be obtained.
    Returns the integer value of the card according to the STandard Blackjack game rules."""

    return card_values[card_name]



def get_total_value( card_names_list ):
    """Takes a list of card names as parameter.
    Returns the total value of all the cards according to the Standard Blackjack game rules."""

    sum = 0
    for name in card_names_list:
       sum += card_values[name]
    return sum

def declare_bust( whose_bust ):
    if whose_bust.lower() == "user":
       print("BUST! Your total exceeded 21.")
       print("You LOSE!")
       print(lose_ascii_art)
    elif whose_bust.lower() == "computer":
       print("BUST! Computer total exceeded 21.")
       print("You WIN!")
       print(win_ascii_art)


def declare_winner(user_sum, computer_sum):
    """Takes user's total and compueter's total as parameters.
    Displays the winner message."""
    
    if user_sum == computer_sum:
       print("Its a TIE")
       print(tie_ascii_art)
    elif user_sum > computer_sum:
       print("You WIN !!!")
       print(win_ascii_art)
    else:
       print("You LOSE !!!")
       print(lose_ascii_art)
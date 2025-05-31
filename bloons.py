from math import floor as f #Floor calculations
from math import exp as e
from os import system as sys #Clear the terminal every after every round
from random import randint #Randomize the amount of bloons per wave slightly
from time import sleep as slow #Used for slow print and delays
import ast #For saving and loading existing files

#Dictionary to store player stats
player = {
    "Lives": 3,
    "Wave": 0,
    "Gold": 100,
}

#Dictionary to store towers
towers = {
    "Mini-Mortars": {"unlocked": True, "number": 1, "power": 10, "cost": 25, "unlocks_at": 1, "level": 1, "upgrade_cost": 75, "upgrade_multiplier": 1.8},
    "Dart Goblin Towers": {"unlocked": False, "number": 0, "power": 15, "cost": 50, "unlocks_at": 3, "level": 1, "upgrade_cost": 110, "upgrade_multiplier": 1.7},
    "Rapid Firecrackers": {"unlocked": False, "number": 0, "power": 20, "cost": 75, "unlocks_at": 5, "level": 1, "upgrade_cost": 180, "upgrade_multiplier": 1.65},
    "Magic Archer Towers": {"unlocked": False, "number": 0, "power": 30, "cost": 125, "unlocks_at": 10, "level": 1, "upgrade_cost": 300, "upgrade_multiplier": 1.65},
    "Burst Ricochet-Cannons": {"unlocked": False, "number": 0, "power": 35, "cost": 200, "unlocks_at": 15, "level": 1, "upgrade_cost": 450, "upgrade_multiplier": 1.50},
    "Boomerang Blizzard Wizards": {"unlocked": False, "number": 0, "power": 40, "cost": 400, "unlocks_at": 20, "level": 1, "upgrade_cost": 750, "upgrade_multiplier": 1.49},
    "Obsidian Crushers": {"unlocked": False, "number": 0, "power": 50, "cost": 600, "unlocks_at": 25, "level": 1, "upgrade_cost": 1125, "upgrade_multiplier": 1.47},
    "Mega Teslas": {"unlocked": False, "number": 0, "power": 70, "cost": 800, "unlocks_at": 30, "level": 1, "upgrade_cost": 1500, "upgrade_multiplier": 1.49},
    "Lava Launchers": {"unlocked": False, "number": 0, "power": 100, "cost": 1000, "unlocks_at": 35, "level": 1, "upgrade_cost": 2250, "upgrade_multiplier": 1.55},
    "Accelerated X-Bows": {"unlocked": False, "number": 0, "power": 120, "cost": 2000, "unlocks_at": 40, "level": 1, "upgrade_cost": 3000, "upgrade_multiplier": 1.52},
    "Giga Infernos": {"unlocked": False, "number": 0, "power": 150, "cost": 2500, "unlocks_at": 45, "level": 1, "upgrade_cost": 4500, "upgrade_multiplier": 1.51},
    "Crystal Monoliths": {"unlocked": False, "number": 0, "power": 200, "cost": 3000, "unlocks_at": 50, "level": 1, "upgrade_cost": 7500, "upgrade_multiplier": 1.3},
    "Vibranium Eagles": {"unlocked": False, "number": 0, "power": 350, "cost": 4000, "unlocks_at": 55, "level": 1, "upgrade_cost": 11250, "upgrade_multiplier": 1.36},
    "Phoenix Lords": {"unlocked": False, "number": 0, "power": 500, "cost": 5000, "unlocks_at": 60, "level": 1, "upgrade_cost": 15000, "upgrade_multiplier": 1.4},
    "Omega Onis": {"unlocked": False, "number": 0, "power": 600, "cost": 10000, "unlocks_at": 70, "level": 1, "upgrade_cost": 20000, "upgrade_multiplier": 1.4},
    "Doomfire Dragons": {"unlocked": False, "number": 0, "power": 1000, "cost": 20000, "unlocks_at": 80, "level": 1, "upgrade_cost": 30000, "upgrade_multiplier": 1.4}
}

#Dictionary to store bloons
bloons = {
    "Red Bloons": {"strength": 7, "unlocked": True, "unlocks_at": 1, "multiplier": 1.2, "min_count": 2, "max_count": 5},
    "Blue Bloons": {"strength": 8, "unlocked": False, "unlocks_at": 3, "multiplier": 1.3, "min_count": 4, "max_count": 7},
    "Ice Bloons": {"strength": 10, "unlocked": False, "unlocks_at": 6, "multiplier": 1.3, "min_count": 4, "max_count": 8},
    "Ghost Green Bloons": {"strength": 12, "unlocked": False, "unlocks_at": 8, "multiplier": 1.5, "min_count": 4, "max_count": 9},
    "Plated Yellow Bloons": {"strength": 20, "unlocked": False, "unlocks_at": 11, "multiplier": 1.7, "min_count": 3, "max_count": 8},
    "Pink-Exploding Bloons": {"strength": 30, "unlocked": False, "unlocks_at": 16, "multiplier": 1.8, "min_count": 3, "max_count": 8},
    "Black-Shielded Bloons": {"strength": 40, "unlocked": False, "unlocks_at": 24, "multiplier": 2.0, "min_count": 3, "max_count": 8},
    "Green-Camo Bloons": {"strength": 70, "unlocked": False, "unlocks_at": 29, "multiplier": 2.2, "min_count": 2, "max_count": 6},
    "Invisible Lead Bloons": {"strength": 100, "unlocked": False, "unlocks_at": 34, "multiplier": 2.5, "min_count": 2, "max_count": 3},
    "Accelerated Gold Bloons": {"strength": 125, "unlocked": False, "unlocks_at": 39, "multiplier": 3.0, "min_count": 1, "max_count": 2},
    "Massive Blimps": {"strength": 200, "unlocked": False, "unlocks_at": 44, "multiplier": 3.5, "min_count": 1, "max_count": 1},
    "Flying Behemoths": {"strength": 300, "unlocked": False, "unlocks_at": 49, "multiplier": 4.0, "min_count": 1, "max_count": 1},
    "Titan Bloon Helicarriers": {"strength": 450, "unlocked": False, "unlocks_at": 52, "multiplier": 5.0, "min_count": 1, "max_count": 1},
    "Phantom Airships of Doom": {"strength": 500, "unlocked": False, "unlocks_at": 62, "multiplier": 6.0, "min_count": 1, "max_count": 1}, 
    "Final Reaper Bloons": {"strength": 550, "unlocked": False, "unlocks_at": 70, "multiplier": 6.0, "min_count": 1, "max_count": 1}
}

'''Slow Print Function allows the game to print one character at a time if needed. 
Flush will force immediate output instead of waiting for the buffer.'''
def slow_print(text, delay=0.02): 
    for char in text:
        print(char, end = '', flush = True) 
        slow(delay) 
    print()

'''Print player information at the beginning of each round including game name, player stats, and tower stats.'''
def display_stats(): 
    print("=" * 70) 
    print("=" * 70)
    print("\033[1mMICHAEL'S BLOONS TOWER DEFENSE\033[0m") 
    for stat in player.keys(): 
        print(f"\t{stat}: {player[stat]}")
    print("\tTOWER STATS: ")
    for tower in towers.keys(): 
        if towers[tower]["unlocked"] == True: 
            print(f"\t\t{tower}: {towers[tower]["number"]}, Level: {towers[tower]["level"]}")
    print("=" * 70)

'''Calculate the defense strength every round.
Its found by adding the defense strength of every tower the user owns together'''
def defense_strength_calculation(): 
    defense_strength = 0 
    for tower in towers.keys():
        if towers[tower]["unlocked"] == True:
            defense_strength += towers[tower]["number"] * towers[tower]["power"]
    return defense_strength 

'''Calculate the attack strength of the bloons every round.
The bloons are also stores into a dictionary to be printed out'''
def attack_strength_calculation(): 
    bloon_wave = {}  
    attack_strength = 0 

    for bloon in bloons:
        if bloons[bloon]["unlocked"]: 
            min_count = bloons[bloon]["min_count"]
            max_count = bloons[bloon]["max_count"] + f(player["Wave"] // 3) 
            bloon_count = randint(min_count, max_count) 
            bloon_wave[bloon] = bloon_count #Store into the bloon wave dictionary
            attack_strength += bloon_count * bloons[bloon]["strength"]  
    return bloon_wave, attack_strength #Return dictionary of bloons in the wave and their attack strengths

'''Everytime the user choose to defend a wave this function is run.
All attacking bloons are printed out to the user.
The difference between attack and defense strength is also calculated'''
def defense_round():
    global gold_rush_active
    player.update({"Wave": player["Wave"] + 1}) 
    bloon_wave, attack_strength = attack_strength_calculation()
    defense_strength = defense_strength_calculation() #Run Calculations
    slow_print("You are currently being attacked by: ")
    for bloon in bloon_wave.keys(): 
        slow_print(f"{bloon_wave[bloon]} {bloon}") 
    difference = defense_strength - attack_strength 
    random_event() #Trigger a random event 

    gold_earned = calculate_gold_reward()
    if gold_rush_active:
        gold_earned *= 2
        gold_rush_active = False  # Reset Gold Rush immediately after applying
    return difference, gold_earned
    
'''The user is able to soft reset if they choose or if they die.
The soft reset will roll them back 10 waves while maintaining any gold, towers, and upgrades.
'''
def soft_reset():
    slow_print("Soft Reset Initiated...")
    
    new_wave = max(1, player["Wave"] - 10)
    player["Wave"] = new_wave
    player["Lives"] = 3
    slow_print(f"Wave rolled back to {player['Wave']}. Your towers, upgrades, and gold remain.")
    
    for bloon in bloons: #re-lock any bloon that should not exist in this new wave
        if bloons[bloon]["unlocks_at"] > player["Wave"]:
            bloons[bloon]["unlocked"] = False
    slow_print("All higher-level bloons that require a wave higher than your new wave have been locked again.")
    slow_print("Lives have been reset to 3")
    slow_print("Restarting game now...\n")

'''Checks if a tower is unlocked as waves progress'''
def check_tower_unlocks(): 
    for tower in towers:
        if towers[tower]["unlocked"] == False and player["Wave"] >= towers[tower]["unlocks_at"]:
            towers[tower]["unlocked"] = True
            slow_print(f"🎉 Congratulations!!! New Tower Unlocked: {tower}! You can now purchase it!!")

'''Checks if a bloon is unlocked as waves progress'''
def check_bloon_unlocks(): 
    for bloon in bloons:
        if bloons[bloon]["unlocked"] == False and player["Wave"] >= bloons[bloon]["unlocks_at"]:
            bloons[bloon]["unlocked"] = True
            slow_print(f"⚠️ Warning: New Bloon Unlocked - {bloon}! Be prepared to defend it!")

'''This function is run if the user chooses to buy new or more existing towers.
The towers they can buy are stored in a dictionary with the cost. They user chooses how many of any tower they wish to buy.'''
def buy_towers(): 
    available_towers = {}
    for tower in towers:
        if towers[tower]["unlocked"] == True:
            available_towers[tower] = towers[tower]["cost"]
    print(f"You have {player['Gold']} gold.")
    slow_print("Available Tower to Purchase: \n")
    for name in available_towers:
        print(f"{name} - Cost: {available_towers[name]} Gold")
    
    
    selected_tower = input("\nPlease enter the EXACT name of the tower you want to buy: ").strip()
    if selected_tower not in available_towers:
        slow_print("YOU TYPED IT IN WRONG!!! \n")
        return
    try: #Make sure the user types an integer value
        quantity = int(input(f"How many {selected_tower} would you like to buy? "))
        if quantity <= 0:
            slow_print("YOU HAVE TO BUY SOMETHING!!! \n")
            return
    except ValueError:
        slow_print("YOU TYPED IT IN WRONG!!! \n")
        return
    
    total_cost = available_towers[selected_tower] * quantity #Calculate the cost 
    if player["Gold"] >= total_cost:
        player["Gold"] -= total_cost  #Deduct gold from the player
        towers[selected_tower]["number"] += quantity  #Add purchased towers to the users stats
        slow_print(f"You have successfully purchased {quantity} {selected_tower}! \n")
    else:
        slow_print("YOUR TOO POOR!!! \n")
    
'''This function is run if the user chooses to upgrade their existing towers.
Then the upgrade costs of that tower will be increased.'''
def upgrade_towers(): 
    available_towers = {}
    for tower in towers:
        if towers[tower]["unlocked"]:
            available_towers[tower] = towers[tower]["upgrade_cost"]

    print(f"You have {player['Gold']} gold.")
    slow_print("Available Towers to Upgrade: \n")
    for name in available_towers:
        print(f"{name} - Level: {towers[name]['level']} || Upgrade Cost: {towers[name]["upgrade_cost"]} Gold")
    selected_tower = input("\nEnter the EXACT name of the tower you want to upgrade: ").strip()
    if selected_tower not in available_towers:
        slow_print("YOU TYPED IT IN WRONG!!!\n")
        return
    
    upgrade_cost = towers[selected_tower]["upgrade_cost"]
    if player["Gold"] >= upgrade_cost:
        player["Gold"] -= upgrade_cost  
        towers[selected_tower]["power"] = f(towers[selected_tower]["power"] * towers[selected_tower]["upgrade_multiplier"]) 
        towers[selected_tower]["level"] += 1  
        towers[selected_tower]["upgrade_cost"] = f(towers[selected_tower]["upgrade_cost"] * 1.5)
        slow_print(f"Successfully upgraded {selected_tower} to Level {towers[selected_tower]['level']}!\n")
    else:
        slow_print("YOUR TOO POOR!!!\n")

'''Player can choose to sell towers for gold by will only earn a fraction of the purchase cost back'''
def sell_towers(): 
    available_towers = {} 
    for tower in towers:
        if towers[tower]["unlocked"] and towers[tower]["number"] > 0:
            available_towers[tower] = f(towers[tower]["cost"] * 0.75)  

    if not available_towers: #No towers the user can sell
        slow_print("You have no towers to sell!\n")
        return

    print(f"You have {player['Gold']} gold.") #Display towers that can be sold
    slow_print("Towers Available to Sell:\n")
    for name in available_towers:
        print(f"{name} - Owned: {towers[name]['number']} | Sell Price per Tower: {available_towers[name]} Gold")

    selected_tower = input("\nEnter the EXACT name of the tower you want to sell: ").strip()
    tower_price = available_towers.get(selected_tower)
    if tower_price is None: #If the tower does not exist
        slow_print("YOU TYPED IT IN WRONG!!!\n")
        return
    
    try: #Make sure the user enters an integer
        quantity = int(input(f"How many {selected_tower}s would you like to sell? "))
        if quantity <= 0:
            slow_print("YOU HAVE TO SELL AT LEAST ONE!!!\n")
            return
    except ValueError:
        slow_print("YOU TYPED IT IN WRONG!!!\n")
        return
    if quantity > towers[selected_tower]["number"]:
        slow_print("YOU DON'T HAVE THAT MANY TO SELL!!!\n")
        return

    gold_earned = (towers[selected_tower]["cost"] // 2) * quantity
    player["Gold"] += gold_earned  
    towers[selected_tower]["number"] -= quantity  

    if towers[selected_tower]["number"] == 0: # If the tower count hits 0
        slow_print(f"You have sold all of your {selected_tower}s.\n")
    else:
        slow_print(f"You have successfully sold {quantity} {selected_tower} and earned {gold_earned} Gold!\n")

#Calculate the gold earned per round.
#There is a base amount of gold that increases by a certain constant amount per round
def calculate_gold_reward():
    base_gold = 100  #Minimum gold earned per wave
    gold_exponential_base = 1.09  #Determines how much more is earned per wave
    gold_reward = f(base_gold * (gold_exponential_base ** player["Wave"]))
    return gold_reward

'''#Logistical version of gold reward
def calculate_gold_reward():
    global gold_rush_active

    G_max = 15000  # Maximum gold earned per wave
    k = 0.184  # Growth rate (calculated to fit the scaling)
    W_mid = 15  # The wave where growth slows down

    # Logistic function for gold scaling
    gold_reward = f(G_max / (1 + e(-k * (player["Wave"] - W_mid))))

    return gold_reward'''

'''Print game instructions out the the user'''
def game_instructions():
    slow_print("Welcome to Michael's Bloons Tower Defense Game.")
    slow_print("The goal of this game is to defend waves of bloon attacks.")
    slow_print("The difficulty progresses throughout waves. Upgrade existing towers and buy new towers to keep up!")
    slow_print("You can sell any existing towers for gold, but you will only earn a fraction of the cost back!")
    slow_print("You begin the game with 3 lives and lose 1 every time bloons get past your defenses.\nSpecial Events can occur at anytime. Be prepared for them!!!")
    slow_print("If you lose all your lives or choose to soft reset, you go back 10 waves, while maintaining any upgrades, towers, and gold earned.")
    slow_print("Remember to save the game under your name!!!")
    slow_print("Have Fun!!!")
    slow(3.00)
    return

'''If the player choose to save their game, the information will be stored under their lastname_firstname.txt
All information is stored as a line in the text file'''
def save_file():
    first = input("Enter your first name: ").strip().lower()
    last = input("Enter your last name: ").strip().lower()
    file_name = last + "_" + first
    with open(file_name+".txt", "w") as my_file:
        #Save player data
        my_file.write("player=" + str(player) + "\n")
        #Save towers data
        my_file.write("towers=" + str(towers) + "\n")
        #Save bloons data
        my_file.write("bloons=" + str(bloons) + "\n")
    slow_print("Game saved successfully!", 0.02)

'''The player is able to lead an existing game save file through their first and last name.
Function will try to open file but fail if the file does not exist.'''
def load_file():
    global player, towers, bloons  #These variables exist outside of the function
    first = input("Enter your first name: ").strip().lower()
    last = input("Enter your last name: ").strip().lower()
    file_name = last + "_" + first
    try:
        with open(file_name+".txt", "r") as my_file:
            for line in my_file:
                #Split the line into key and value parts
                key, value = line.strip().split("=", 1)
                #Use literal_eval to safely convert the string back to a dictionary
                if key == "player":
                    player = ast.literal_eval(value)
                elif key == "towers":
                    towers = ast.literal_eval(value)
                elif key == "bloons":
                    bloons = ast.literal_eval(value)
        slow_print("Game loaded successfully!")
    except FileNotFoundError:
        slow_print("No save file found. Starting a new game...")

'''This function will trigger a random event to occur every once in a while'''
gold_rush_active = False
def random_event():
    global gold_rush_active  
    events = [ #List/Dictionary of possible event that can occue
        {"name": "💥 Nuke Event", "effect": "You dropped a NUKE! The nuke destroyed 5 waves of bloons!", "type": "nuke"},
        {"name": "⚠️ Spy Bloon Ambush", "effect": "OH NO! A spy bloon ambush snuck behind your defenses! You lost 1 life!", "type": "life_loss"},
        {"name": "🔥 Phoenix Blessing", "effect": "A Phoenix has blessed your towers!", "type": "power_boost"},
        {"name": "💰 Gold Rush", "effect": "Gold Rush activated!", "type": "gold_rush"},
        {"name": "🏴‍☠️ Goblin Thief", "effect": "OH NO! A sneaky Goblin snuck behind your front lines and stole 500 Gold!", "type": "gold_loss"},
        {"name": "🎩 The Great Goblin Heist!", "effect": "Goblins tried to sneak behind your front lines to steal your gold. But, the goblins dropped their loot while trying to escaping! You gain bonus gold!", "type": "goblin_heist"},
        {"name": "💎 Mysterious Treasure Chest!", "effect": "OH NO! You found a treasure chest but as soon as you touched it, it cursed you!", "type": "treasure_trap"}
    ]

    if randint(1, 4) == 1:  #25% chance of triggering an event
        event = events[randint(0, len(events) - 1)] #Pick and event
        slow_print(f"\nSpecial Event Activated! {event['name']}: {event['effect']}")

        if event["type"] == "nuke":
            gold_earned = f(calculate_gold_reward() * 5)
            player["Gold"] += gold_earned
            player["Wave"] += 5  # Skip 5 waves
            slow_print(f"💰 You earned {gold_earned} Gold and skipped 5 waves!")

        elif event["type"] == "life_loss":
            player["Lives"] -= 1
            if player["Lives"] <= 0:
                slow_print("❌ You have lost all your lives!")
                soft_reset()
            else:
                slow_print(f"💔 You now have {player['Lives']} lives left.")

        elif event["type"] == "power_boost": #Plus 5 power boost
            for tower in towers.values():
                if tower["unlocked"]:
                    tower["power"] += 5
            slow_print("🔥 Your towers have been boosted by the Phoenix's blessing!")

        elif event["type"] == "gold_rush" and not gold_rush_active:
            gold_rush_active = True  #Activate Gold Rush for next wave
            slow_print("💰 Earn DOUBLE gold this wave!")

        elif event["type"] == "gold_loss":
            player["Gold"] = max(0, player["Gold"] - 500)  #Make sure it doesn't go negative
            slow_print(f"💸 Your now have {player['Gold']} gold!")
        
        elif event["type"] == "goblin_heist":
            bonus_gold = randint(300, 1000)
            player["Gold"] += bonus_gold
            slow_print(f"💰 The goblins accidentally dropped {bonus_gold} Gold for you!")
        
        elif event["type"] == "treasure_trap":
            player["Lives"] -= 1
            if player["Lives"] <= 0:
                slow_print("❌ The cursed chest drained you of your last breath!")
                soft_reset()
            else:
                slow_print(f"💔 OWW! You have {player['Lives']} left.")


def infinite_game_loop(): #Game Loop
    slow(0.77) #Delay before clearing screen
    sys("cls" if "win" in sys.__name__ else "clear")
    display_stats()
    print("=" * 70)
    player_choice = input("What would you like to do? Enter the digit only below: \n\tDefend Wave  .............. 1\n\tUpgrade Towers  ........... 2\n\tBuy Towers  ............... 3\n\tSell Towers  .............. 4\n\tSoft Reset  ............... 5\n\tGame Instructions  ........ 6\n\tSave File  ................ 7\n\tLoad File  ................ 8\n")
    
    if player_choice == "1": #Defend a Wave
        defense_strength_calculation()
        attack_strength_calculation()
        difference, gold_earned = defense_round() #Use difference to calculate if player won
        if difference >= 0:
            slow_print(f"You successfully defended this wave! You earned {gold_earned} gold.")
        else:
            player["Lives"] -= 1
            slow_print(f"Oh NO! ❌The Bloons broke through! You lost 1 life!💔 You still earned {gold_earned} gold.")
            if player["Lives"] <= 0:
                slow_print("You have lost all your lives. Soft Resetting...")
                soft_reset()
                return  
        player["Gold"] += f(gold_earned)
        check_tower_unlocks()
        check_bloon_unlocks()
        return  # Exit after defending the round
    
    elif player_choice == "2": #Upgrade
        upgrade_towers()
    elif player_choice == "3": #Buy
        buy_towers()
    elif player_choice == "4": #Sell
        sell_towers()
    elif player_choice == "5": #Soft Reset
        soft_reset()
    elif player_choice == "6": #Game Instructions
        game_instructions()
    elif player_choice == "7": #Save to .txt File
        save_file()
    elif player_choice == "8": #Load a file
        load_file()
    else:
        slow_print("THAT'S NOT AN OPTION DUMMY!!!")

def main():
    while True:
        infinite_game_loop()

if __name__ == "__main__":
    main()
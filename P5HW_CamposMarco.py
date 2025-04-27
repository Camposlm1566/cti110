#Marco Campos
#April 20, 2025
#P5HW
#Using loops, functions, and module import

import random

# Create the character
def create_character():
    name = "KhaosPolo"
    health = 100
    attack_points = 15
    points = 0
    inventory = []  # Items like potions go here
    character = {
        "name": name,
        "health": health,
        "attack_points": attack_points,
        "points": points,
        "inventory": inventory
    }
    return character

# Display character stats
def display_character(character):
    print("\n--- KhaosPolo's Stats ---")
    for key, value in character.items():
        print(f"{key.capitalize()}: {value}")

# Fight a monster
def fight_monster(character):
    monsters = [
        {"name": "Goblin", "health": 30, "attack": 10, "reward": 20},
        {"name": "Skeleton", "health": 40, "attack": 15, "reward": 30},
        {"name": "Dark Knight", "health": 60, "attack": 20, "reward": 50}
    ]
    monster = random.choice(monsters)
    print(f"\n💀 A wild {monster['name']} appears! Prepare for battle!")

    while monster["health"] > 0 and character["health"] > 0:
        damage_to_monster = random.randint(5, character["attack_points"])
        monster["health"] -= damage_to_monster
        print(f"KhaosPolo hits {monster['name']} for {damage_to_monster} damage!")

        if monster["health"] <= 0:
            print(f"✅ {monster['name']} is defeated! +{monster['reward']} points earned.")
            character["points"] += monster["reward"]
            return

        damage_to_player = random.randint(5, monster["attack"])
        character["health"] -= damage_to_player
        print(f"{monster['name']} strikes back for {damage_to_player} damage!")

        if character["health"] <= 0:
            character["health"] = 0
            print("💀 KhaosPolo has fallen in battle...")

# Find treasure
def find_treasure(character):
    gained_points = random.randint(10, 50)
    character["points"] += gained_points
    print(f"\nKhaosPolo found treasure and earned {gained_points} points!")

# Trap encounter
def trigger_trap(character):
    damage = random.randint(5, 25)
    character["health"] -= damage
    print(f"\nA trap was triggered! KhaosPolo lost {damage} health.")
    if character["health"] < 0:
        character["health"] = 0

# Find a potion
def find_potion(character):
    character["inventory"].append("Potion")
    print("\n🧪 KhaosPolo found a healing potion!")

# Use a potion
def use_potion(character):
    if "Potion" in character["inventory"]:
        heal = random.randint(20, 40)
        character["health"] += heal
        character["inventory"].remove("Potion")
        print(f"\n🧪 KhaosPolo used a potion and healed {heal} health!")
    else:
        print("\n❌ No potions in inventory!")

# Dungeon exploration
def explore_dungeon(character):
    event = random.choice(["treasure", "trap", "monster", "potion", "nothing"])
    if event == "treasure":
        find_treasure(character)
    elif event == "trap":
        trigger_trap(character)
    elif event == "monster":
        fight_monster(character)
    elif event == "potion":
        find_potion(character)
    else:
        print("\nKhaosPolo explored the room but found nothing...")

# Main function
def main():
    print("🧙 Welcome to KhaosPolo's Dungeon Adventure!")

    character = create_character()

    while True:
        print("\nChoose an action:")
        print("1. Explore Dungeon Room")
        print("2. Display Stats")
        print("3. Use Potion")
        print("4. Exit Dungeon")
        choice = input("Enter your choice: ")

        if choice == "1":
            explore_dungeon(character)
            if character["health"] == 0:
                print("\n💀 KhaosPolo has no health left. Game Over.")
                break
        elif choice == "2":
            display_character(character)
        elif choice == "3":
            use_potion(character)
        elif choice == "4":
            print("\n🏁 KhaosPolo escapes the dungeon with", character["points"], "points. Victory!")
            break
        else:
            print("Invalid choice. Try again.")

# Start the game
main()

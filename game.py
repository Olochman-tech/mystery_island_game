LOCATIONS = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"]
}

ITEM_LOCATIONS = {
    "Jungle": "rope",
    "Cave": "lantern"
}


def calculate_energy(current_energy, energy_used):
    result = current_energy - energy_used

    if result < 0:
        return 0

    return result


def new_game(name):
    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False
    }


def move_player(player, destination):
    if player["game_over"]:
        return "The game has ended. Start a new game to play again."

    current_location = player["location"]

    if destination not in LOCATIONS[current_location]:
        return "You cannot move there from your current location."

    if destination == "Old Bridge" and "rope" not in player["inventory"]:
        return "The bridge is dangerous. You need a rope to cross."

    player["location"] = destination
    player["energy"] = calculate_energy(player["energy"], 1)

    if player["energy"] == 0:
        player["game_over"] = True
        return "You have run out of energy. Game over!"

    return f"You moved to {destination}. Energy remaining: {player['energy']}"


def collect_item(player):
    if player["game_over"]:
        return "The game has ended."

    location = player["location"]

    if location not in ITEM_LOCATIONS:
        return "There is no useful item to collect here."

    item = ITEM_LOCATIONS[location]

    if item in player["inventory"]:
        return f"You have already collected the {item}."

    player["inventory"].append(item)
    return f"You collected the {item}."


def show_inventory(player):
    if not player["inventory"]:
        return "Your inventory is empty."

    return "Inventory: " + ", ".join(player["inventory"])


def light_beacon(player):
    if player["game_over"]:
        return "The game has ended."

    if player["location"] != "Lighthouse":
        return "You must reach the Lighthouse first."

    if "lantern" not in player["inventory"]:
        return "You need a lantern to light the beacon."

    if player["energy"] <= 0:
        player["game_over"] = True
        return "You have no energy left. Game over!"

    player["won"] = True
    player["game_over"] = True

    return "You light the lighthouse beacon! A rescue boat sees the signal. YOU WIN!"
from game import new_game, move_player, collect_item, show_inventory, light_beacon, LOCATIONS


def display_intro():
    print("\n===================================")
    print("       MYSTERY ISLAND")
    print("        THE LOST LIGHTHOUSE")
    print("===================================")
    print("\nYou have been stranded on a mysterious island after a storm.")
    print("The lighthouse beacon is dark.")
    print("A rescue boat will only find you if you restore the beacon.")
    print("\nYour mission:")
    print("1. Explore the island.")
    print("2. Find a rope and a lantern.")
    print("3. Use the rope to cross the Old Bridge.")
    print("4. Reach the Lighthouse and light the beacon.")
    print("\nBe careful! You only have 5 energy points.")
    print("Every successful move costs 1 energy point.")


def display_status(player):
    print("\n-----------------------------------")
    print(f"Player: {player['name']}")
    print(f"Location: {player['location']}")
    print(f"Energy: {player['energy']}")
    print("-----------------------------------")


def display_menu():
    print("\nWhat would you like to do?")
    print("1. Move to another location")
    print("2. Collect an item")
    print("3. Check inventory")
    print("4. Light the lighthouse beacon")
    print("5. Quit game")


def play_game():
    display_intro()

    name = input("\nEnter your player name: ").strip()

    if not name:
        name = "Explorer"

    player = new_game(name)

    while not player["game_over"]:
        display_status(player)
        display_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            current_location = player["location"]
            destinations = LOCATIONS[current_location]

            print("\nAvailable destinations:")

            for destination in destinations:
                print(f"- {destination}")

            destination = input("\nWhere do you want to go? ").strip().title()

            message = move_player(player, destination)
            print(message)

        elif choice == "2":
            print(collect_item(player))

        elif choice == "3":
            print(show_inventory(player))

        elif choice == "4":
            print(light_beacon(player))

        elif choice == "5":
            print("\nYou have left Mystery Island. Goodbye!")
            player["game_over"] = True

        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")


def main():
    while True:
        play_game()

        replay = input("\nWould you like to play again? (yes/no): ").strip().lower()

        if replay != "yes":
            print("\nThank you for playing Mystery Island!")
            break


if __name__ == "__main__":
    main()
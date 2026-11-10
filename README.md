# Mystery Island — The Lost Lighthouse

## Project Description

Mystery Island is a beginner-friendly Python command-line adventure game.

The player is stranded on a mysterious island after a storm. The lighthouse beacon is dark, and a rescue boat can only find the player when the beacon is restored.

The player's mission is to explore the island, collect useful items, manage energy, cross the Old Bridge, and light the lighthouse beacon.

## Requirements

- Python 3 installed on your computer.
- No external Python packages are required.

## How to Run the Game

Open a terminal in the project directory and run:

```bash
python3 main.py
```

Enter your player name and follow the menu instructions.

## Game Rules

- The player starts at the Beach with 5 energy points.
- The island contains five locations: Beach, Jungle, Cave, Old Bridge, and Lighthouse.
- The rope is located in the Jungle.
- The lantern is located in the Cave.
- The player needs the rope to cross the Old Bridge.
- The player needs the lantern to light the lighthouse beacon.
- Every successful movement costs 1 energy point.
- Invalid movements do not consume energy.
- The player loses when energy reaches zero before completing the mission.
- The player wins by reaching the Lighthouse with the lantern and lighting the beacon.
- The player can choose to replay after a game ends.

## Running the Tests

Run the automated tests with:

```bash
python3 -m unittest discover -s tests -v
```

The tests check the starting player state, energy calculations, movement, item collection, inventory, bridge restrictions, beacon requirements, winning, and losing.

## Project Structure

```text
mystery_island/
├── main.py
├── game.py
├── tests/
│   └── test_game.py
├── README.md
└── .gitignore
```

## Technologies

- Python 3
- Python standard library
- unittest

## Limitations

- The game runs in the terminal.
- Player progress is not saved after the program closes.
- The game does not use an external database or graphical interface.
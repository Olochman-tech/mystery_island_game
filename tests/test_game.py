import unittest
from game import (
    calculate_energy,
    new_game,
    move_player,
    collect_item,
    show_inventory,
    light_beacon
)


class TestEnergy(unittest.TestCase):

    def test_energy_reduction(self):
        self.assertEqual(calculate_energy(5, 2), 3)

    def test_energy_cannot_be_negative(self):
        self.assertEqual(calculate_energy(3, 5), 0)


class TestNewGame(unittest.TestCase):

    def test_new_game_starts_correctly(self):
        player = new_game("Ada")

        self.assertEqual(player["name"], "Ada")
        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)
        self.assertEqual(player["inventory"], [])
        self.assertFalse(player["game_over"])
        self.assertFalse(player["won"])


class TestMovement(unittest.TestCase):

    def test_valid_move_reduces_energy(self):
        player = new_game("Ada")

        move_player(player, "Jungle")

        self.assertEqual(player["location"], "Jungle")
        self.assertEqual(player["energy"], 4)

    def test_invalid_move_does_not_reduce_energy(self):
        player = new_game("Ada")

        move_player(player, "Lighthouse")

        self.assertEqual(player["location"], "Beach")
        self.assertEqual(player["energy"], 5)

    def test_bridge_requires_rope(self):
        player = new_game("Ada")
        player["location"] = "Cave"

        move_player(player, "Old Bridge")

        self.assertEqual(player["location"], "Cave")
        self.assertEqual(player["energy"], 5)


class TestInventory(unittest.TestCase):

    def test_collect_rope(self):
        player = new_game("Ada")
        player["location"] = "Jungle"

        collect_item(player)

        self.assertIn("rope", player["inventory"])

    def test_item_cannot_be_collected_twice(self):
        player = new_game("Ada")
        player["location"] = "Jungle"

        collect_item(player)
        collect_item(player)

        self.assertEqual(player["inventory"].count("rope"), 1)

    def test_empty_inventory_message(self):
        player = new_game("Ada")

        self.assertEqual(show_inventory(player), "Your inventory is empty.")


class TestBeacon(unittest.TestCase):

    def test_beacon_requires_lantern(self):
        player = new_game("Ada")
        player["location"] = "Lighthouse"

        light_beacon(player)

        self.assertFalse(player["won"])

    def test_player_wins_with_lantern_at_lighthouse(self):
        player = new_game("Ada")
        player["location"] = "Lighthouse"
        player["inventory"].append("lantern")

        light_beacon(player)

        self.assertTrue(player["won"])
        self.assertTrue(player["game_over"])

    def test_energy_exhaustion_ends_game(self):
        player = new_game("Ada")
        player["energy"] = 1

        move_player(player, "Jungle")

        self.assertEqual(player["energy"], 0)
        self.assertTrue(player["game_over"])


if __name__ == "__main__":
    unittest.main()
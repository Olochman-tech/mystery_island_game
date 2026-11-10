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

    def test_new_game_resets_player_state(self):
        first_player = new_game("Ada")
        first_player["location"] = "Lighthouse"
        first_player["energy"] = 0
        first_player["inventory"].append("rope")

        second_player = new_game("John")

        self.assertEqual(second_player["location"], "Beach")
        self.assertEqual(second_player["energy"], 5)
        self.assertEqual(second_player["inventory"], [])
        self.assertFalse(second_player["game_over"])
        self.assertFalse(second_player["won"])

    def test_players_have_separate_inventories(self):
        first_player = new_game("Ada")
        second_player = new_game("John")

        first_player["inventory"].append("rope")

        self.assertEqual(second_player["inventory"], [])


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

    def test_bridge_can_be_crossed_with_rope(self):
        player = new_game("Ada")
        player["location"] = "Cave"
        player["inventory"].append("rope")

        move_player(player, "Old Bridge")

        self.assertEqual(player["location"], "Old Bridge")
        self.assertEqual(player["energy"], 4)

    def test_movement_is_blocked_after_game_ends(self):
        player = new_game("Ada")
        player["game_over"] = True

        move_player(player, "Jungle")

        self.assertEqual(player["location"], "Beach")
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

    def test_lantern_cannot_be_collected_twice(self):
        player = new_game("Ada")
        player["location"] = "Cave"

        collect_item(player)
        collect_item(player)

        self.assertEqual(player["inventory"].count("lantern"), 1)

    def test_empty_inventory_message(self):
        player = new_game("Ada")

        self.assertEqual(show_inventory(player), "Your inventory is empty.")


class TestBeacon(unittest.TestCase):

    def test_beacon_requires_lantern(self):
        player = new_game("Ada")
        player["location"] = "Lighthouse"

        light_beacon(player)

        self.assertFalse(player["won"])

    def test_beacon_requires_lighthouse_location(self):
        player = new_game("Ada")
        player["location"] = "Cave"
        player["inventory"].append("lantern")

        light_beacon(player)

        self.assertFalse(player["won"])
        self.assertFalse(player["game_over"])

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
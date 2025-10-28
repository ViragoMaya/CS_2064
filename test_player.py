import unittest

from player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Sue Flay", 42, "VT Hokies")

    def test_cntr_and_str(self):
        result = self.player.__str__()
        expected_value = "Sue Flay: healthy"
        self.assertEqual(result, expected_value)

        player = Player("Zed", 161, "Home", status="grow", position="still")
        result = player.__str__()
        expected_value = "Zed: grow"
        self.assertEqual(result, expected_value)

        # testing constructor
        result = [
            player.name,
            player.number,
            player.status,
            player.school,
            player.position,
            player.game_stats,
            player.tournament_stats,
        ]
        expected_value = [
            "Zed",
            161,
            "grow",
            "Home",
            "still",
            {"points": 0, "rebounds": 0, "turnovers": 0},
            {"points": 0, "rebounds": 0, "turnovers": 0, "number_of_games": 0},
        ]
        self.assertEqual(result, expected_value)

    def test_eq_same(self):
        self.assertTrue(self.player == self.player)

    def test_eq_diff(self):
        self.assertFalse(self.player == "Sue Flay")

    def test_eq_ttt(self):
        temp = Player("Sue Flay", 42, "VT Hokies")
        self.assertTrue(self.player == temp)

    def test_eq_ttf(self):
        temp = Player("Sue Flay", 42, "VT Hokie")
        self.assertFalse(self.player == temp)

    def test_eq_tf(self):
        temp = Player("Sue Flay", 41, "VT Hokies")
        self.assertFalse(self.player == temp)

    def test_eq_f(self):
        temp = Player("Sue Fla", 42, "VT Hokies")
        self.assertFalse(self.player == temp)

    def test_reset(self):
        for i, key in enumerate(self.player.game_stats, 7):
            self.player.game_stats[key] = i
        self.player.reset()
        result = self.player.game_stats
        expected_value = {"points": 0, "rebounds": 0, "turnovers": 0}
        self.assertEqual(result, expected_value)

    def test_updates(self):
        self.player.update_game_stats(7, 8, 9)
        result = self.player.game_stats
        expected_value = {"points": 7, "rebounds": 8, "turnovers": 9}
        self.assertEqual(result, expected_value)
        result = self.player.tournament_stats
        expected_value["number_of_games"] = 0
        self.assertEqual(result, expected_value)

        self.player.update_game_stats(7, 8, 9)
        result = self.player.game_stats
        expected_value = {"points": 14, "rebounds": 16, "turnovers": 18}
        self.assertEqual(result, expected_value)
        result = self.player.tournament_stats
        expected_value["number_of_games"] = 0
        self.assertEqual(result, expected_value)

        self.player.update_tournament_stats(7, 8, 9)
        result = self.player.game_stats
        expected_value = {"points": 14, "rebounds": 16, "turnovers": 18}
        self.assertEqual(result, expected_value)
        result = self.player.tournament_stats
        expected_value = {
            "points": 21,
            "rebounds": 24,
            "turnovers": 27,
            "number_of_games": 0,
        }
        self.assertEqual(result, expected_value)

    def test_get_tournament_stats(self):
        expected_value = {
            "points": 0,
            "rebounds": 0,
            "turnovers": 0,
            "number_of_games": 0,
            "ppg": 0,
        }
        result = self.player.get_tournament_stats()
        self.assertEqual(result, expected_value)
        result = self.player.tournament_stats
        del expected_value["ppg"]
        self.assertEqual(result, expected_value)

        for i, key in enumerate(self.player.tournament_stats.keys(), 7):
            self.player.tournament_stats[key] = i
        expected_value = {
            "points": 7,
            "rebounds": 8,
            "turnovers": 9,
            "number_of_games": 10,
            "ppg": 0.7,
        }
        result = self.player.get_tournament_stats()
        self.assertEqual(result, expected_value)
        result = self.player.tournament_stats
        expected_value.pop("ppg")
        self.assertEqual(result, expected_value)


if __name__ == "__main__":
    unittest.main(verbosity=2)

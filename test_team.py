import unittest

from player import Player
from team import Team


class TestTeam(unittest.TestCase):
    def setUp(self):
        self.player = Player("Ghazal", 161, "VT")
        self.team = Team("VT")

    def test_cntr_str(self):
        result = self.team.__str__()
        expected_value = "VT: 0.00"
        self.assertEqual(result, expected_value)
        self.team.tournament_stats['wins'] = 1
        self.team.tournament_stats['number_of_games'] = 1
        result = self.team.__str__()
        expected_value = "VT: 1.00"
        self.assertEqual(result, expected_value)
        self.team.tournament_stats['loses'] = 1
        self.team.tournament_stats['number_of_games'] = 2
        result = self.team.__str__()
        expected_value = "VT: 0.50"
        self.assertEqual(result, expected_value)
        self.team.tournament_stats['loses'] = 2
        self.team.tournament_stats['number_of_games'] = 3
        result = self.team.__str__()
        expected_value = "VT: 0.33"
        self.assertEqual(result, expected_value)

        players = []
        for i in range(5):
            players.append(Player(str(i), i, "VT"))
        team = Team("VT", status='good', roster=players)
        result = [
            team.name,
            team.status,
            len(team.roster),
            team.game_stats,
            team.tournament_stats
        ]
        expected_value = [
            "VT",
            "good",
            5,
            {"points": 0, "rebounds": 0, "turnovers": 0},
            {
                "points": 0,
                "rebounds": 0,
                "turnovers": 0,
                "number_of_games": 0,
                "wins": 0,
                "loses": 0,
            },
        ]
        self.assertEqual(result, expected_value)

    def test_eq_same(self):
        self.assertTrue(self.team == self.team)

    def test_eq_diff(self):
        self.assertFalse(self.team == 161)

    def test_eq_t(self):
        team = Team("VT")
        self.assertTrue(self.team == team)

    def test_eq_f(self):
        team = Team("vt")
        self.assertFalse(self.team == team)

    def test_add_player_t(self):
        result = self.team.add_player(self.player)
        self.assertTrue(result)
        name = self.team.roster[0].name
        num = self.team.roster[0].number
        result = [name, num]
        expected_value = ["Ghazal", 161]
        self.assertEqual(result, expected_value)

    def test_add_player(self):
        self.team.add_player(self.player)
        result = self.team.add_player(self.player)
        self.assertFalse(result)

        for i in range(5):
            p = Player(str(i), "vt", i)
            self.team.add_player(p)
        for i in range(1, 5, 2):
            p = Player(str(i), "vt", i)
            result = self.team.add_player(p)
            self.assertFalse(result)
            self.assertEqual(len(self.team.roster), 6)
        result = self.team.add_player(Player("Roberta", " ", 27))
        self.assertTrue(result)
        self.assertEqual(len(self.team.roster), 7)

    def test_get_player_none(self):
        result = self.team.get_player("Ghazal", 161)
        self.assertIsNone(result)
        self.team.add_player(Player("Bruh", 42, "vt"))
        result = self.team.get_player("Ghazal", 161)
        self.assertIsNone(result)

    def test_get_player_tt(self):
        self.team.add_player(self.player)
        returned_player = self.team.get_player("Ghazal", 161)
        result = [returned_player.name, returned_player.number]
        expected_value = ["Ghazal", 161]
        self.assertEqual(result, expected_value)

        for i in range(5):
            self.team.add_player(Player(str(i), i, "vt"))
        returned_player = self.team.get_player("2", 2)
        result = [returned_player.name, returned_player.number]
        expected_value = ["2", 2]
        self.assertEqual(result, expected_value)

    def test_get_player_tf(self):
        self.team.add_player(self.player)
        result = self.team.get_player("Ghazal", 42)
        self.assertIsNone(result)
        for i in range(5):
            self.team.add_player(Player(str(i), i, "vt"))
        result = self.team.get_player("2", 1)
        self.assertIsNone(result)

    def test_get_player_f(self):
        self.team.add_player(self.player)
        result = self.team.get_player("Lazahg", 161)
        self.assertIsNone(result)
        for i in range(5):
            self.team.add_player(Player(str(i), i, "vt"))
        result = self.team.get_player("1", 2)
        self.assertIsNone(result)

    def test_get_tournament_stats(self):
        result = self.team.get_tournament_stats()
        expected_value = {
            "points" : 0,
            "rebounds" : 0,
            "turnovers" : 0,
            "number_of_games" : 0,
            "wins" : 0,
            "loses" : 0,
            "winning_percent" : 0.00
        }
        self.assertEqual(result, expected_value)
        result = self.team.tournament_stats
        expected_value.pop("winning_percent")
        self.assertEqual(result, expected_value)

        self.team.tournament_stats['wins'] = 1
        self.team.tournament_stats['number_of_games'] = 1
        result = self.team.get_tournament_stats()
        expected_value['wins'] = 1
        expected_value['winning_percent'] = 1.0
        expected_value['number_of_games'] = 1
        self.assertEqual(result, expected_value)
        result = self.team.tournament_stats
        expected_value.pop('winning_percent')
        self.assertEqual(result, expected_value)

        self.team.tournament_stats['loses'] = 1
        self.team.tournament_stats['number_of_games'] = 2
        result = self.team.get_tournament_stats()
        expected_value['loses'] = 1
        expected_value['winning_percent'] = 0.5
        expected_value['number_of_games'] = 2
        self.assertEqual(result, expected_value)
        result = self.team.tournament_stats
        expected_value.pop('winning_percent')
        self.assertEqual(result, expected_value)

        self.team.tournament_stats['loses'] = 2
        self.team.tournament_stats['number_of_games'] = 3
        result = self.team.get_tournament_stats()
        expected_value['loses'] = 2
        expected_value['winning_percent'] = 0.33
        expected_value['number_of_games'] = 3
        self.assertEqual(result, expected_value)
        result = self.team.tournament_stats
        expected_value.pop('winning_percent')
        self.assertEqual(result, expected_value)


if __name__ == "__main__":
    unittest.main(verbosity=2)

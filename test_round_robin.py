import unittest

from match import Match
from match_reader import MatchReader
from player import Player
from round_robin import RoundRobin
from team import Team


class TestRoundRobin(unittest.TestCase):
    def setUp(self):
        self.empty_robin = RoundRobin(0)

        #####
        # for generate_matches()
        #####
        team_a = Team("VT Hokies")
        team_b = Team("UVA Wahoos")
        team_c = Team("UNC Tar Heels")
        team_d = Team("Duke Blue Devils")
        teams = [team_a, team_b, team_c, team_d]
        self.teams_robin = RoundRobin(1, participants=teams)

        #####
        # 4 teams to test update_standings()
        # 6 games, or 6 matches total
        #####
        team_players = {
            "team_a": [
                "VT Hokies",
                Player("Sue Flay", 1, "VT"),
                Player("Justin Time", 2, "VT"),
                Player("Anna Sthesia", 3, "VT"),
            ],
            "team_b": [
                "UVA Wahoos",
                Player("Al Beback", 1, "UVA"),
                Player("Ella Vator", 2, "UVA"),
                Player("Rick O'Shea", 3, "UVA"),
                Player("Paige Turner", 4, "UVA"),
            ],
            "team_c": [
                "UNC Tar Heels",
                Player("Bea Minor", 1, "UNC"),
                Player("Sal Ami", 2, "UNC"),
                Player("Gail Forcewind", 3, "UNC"),
                Player("Sum New", 4, "UNC"),
            ],
            "team_d": [
                "Duke Blue Devils",
                Player("Chris P Bacon", 1, "Duke"),
                Player("Barb Dwyer", 2, "Duke"),
                Player("HP Packard", 3, "Duke"),
                Player("Sam Sung", 4, "Duke"),
            ],
        }

        match_data = [
            {
                "match_id": 1,
                "team1": "team_a",
                "team2": "team_b",
                "team1_stats": [[19, 3, 2], [2, 4, 3], [3, 1, 0]],
                "team2_stats": [[7, 0, 5], [15, 6, 4], [4, 5, 2], [0, 3, 3]],
            },
            {
                "match_id": 2,
                "team1": "team_a",
                "team2": "team_c",
                "team1_stats": [[3, 10, 5], [5, 7, 5], [8, 6, 2]],
                "team2_stats": [[12, 6, 2], [16, 3, 0], [9, 3, 4], [0, 8, 3]],
            },
            {
                "match_id": 3,
                "team1": "team_a",
                "team2": "team_d",
                "team1_stats": [[11, 5, 1], [7, 4, 2], [0, 6, 2]],
                "team2_stats": [[17, 3, 3], [14, 2, 2], [10, 2, 0], [15, 3, 4]],
            },
            {
                "match_id": 4,
                "team1": "team_b",
                "team2": "team_c",
                "team1_stats": [[4, 0, 4], [2, 4, 1], [2, 8, 5], [11, 10, 0]],
                "team2_stats": [[5, 3, 3], [13, 3, 2], [8, 2, 5], [0, 10, 0]],
            },
            {
                "match_id": 5,
                "team1": "team_b",
                "team2": "team_d",
                "team1_stats": [[14, 2, 3], [7, 7, 0], [6, 5, 2], [12, 8, 1]],
                "team2_stats": [[5, 4, 0], [5, 0, 1], [19, 1, 2], [3, 3, 3]],
            },
            {
                "match_id": 6,
                "team1": "team_c",
                "team2": "team_d",
                "team1_stats": [[3, 8, 1], [20, 2, 1], [19, 8, 4], [3, 9, 2]],
                "team2_stats": [[16, 4, 0], [8, 4, 3], [12, 5, 1], [19, 7, 4]],
            },
        ]

        team_abbrs = {
            "team_a": "VT",
            "team_b": "UVA",
            "team_c": "UNC",
            "team_d": "Duke",
        }

        matches = []

        for data in match_data:
            # Get original team1 data
            team1_key = data["team1"]
            team1_info = team_players[team1_key]
            team1_name = team1_info[0]
            team1_abbr = team_abbrs[team1_key]
            team1_players = []
            for i in range(len(data["team1_stats"])):
                original_player = team1_info[i + 1]  # +1 to skip the team name
                stats = data["team1_stats"][i]
                new_player = Player(
                    original_player.name, original_player.number, team1_abbr
                )
                new_player.game_stats = {
                    "points": stats[0],
                    "rebounds": stats[1],
                    "turnovers": stats[2],
                }
                team1_players.append(new_player)
            team1_copy = Team(team1_name, roster=team1_players)
            for r in team1_copy.roster:
                pts = r.game_stats["points"]
                rds = r.game_stats["rebounds"]
                tvrs = r.game_stats["turnovers"]
                team1_copy.game_stats["points"] += pts
                team1_copy.game_stats["rebounds"] += rds
                team1_copy.game_stats["turnovers"] += tvrs

            # Get original team2 data
            team2_key = data["team2"]
            team2_info = team_players[team2_key]
            team2_name = team2_info[0]
            team2_abbr = team_abbrs[team2_key]
            team2_players = []
            for i in range(len(data["team2_stats"])):
                original_player = team2_info[i + 1]
                stats = data["team2_stats"][i]
                new_player = Player(
                    original_player.name, original_player.number, team2_abbr
                )
                new_player.game_stats = {
                    "points": stats[0],
                    "rebounds": stats[1],
                    "turnovers": stats[2],
                }
                team2_players.append(new_player)
            team2_copy = Team(team2_name, roster=team2_players)
            for r in team2_copy.roster:
                pts = r.game_stats["points"]
                rds = r.game_stats["rebounds"]
                tvrs = r.game_stats["turnovers"]
                team2_copy.game_stats["points"] += pts
                team2_copy.game_stats["rebounds"] += rds
                team2_copy.game_stats["turnovers"] += tvrs

            # Create the match with new team instances
            matches.append(Match(data["match_id"], team1_copy, team2_copy))

        self.match_robin = RoundRobin(2, status="completed", matches=matches)

    def test_eq_same(self):
        self.assertTrue(self.teams_robin == self.teams_robin)
        self.assertTrue(self.match_robin == self.match_robin)

    def test_eq_diff(self):
        self.assertFalse(self.teams_robin == "Help!")

    def test_eq(self):
        temp_t = RoundRobin(2)
        temp_f = RoundRobin(42)
        self.assertTrue(self.match_robin == temp_t)
        self.assertFalse(self.match_robin == temp_f)

    def test_generate_matches(self):
        self.teams_robin.generate_matches()
        matches = self.teams_robin.matches
        self.assertEqual(len(matches), 6)
        result = self.teams_robin.status
        self.assertEqual(result, "scheduled")

        data = MatchReader("round_robin_matches.csv")
        team_names = set()
        for m in data.matches:
            team_names.add(m.team1.name)
            team_names.add(m.team2.name)
        teams = []
        for t_name in team_names:
            teams.append(Team(t_name))
        new_robin = RoundRobin(161, teams)
        new_robin.generate_matches()
        self.assertEqual(len(new_robin.matches), 55)

    def test_update_standings_inits(self):
        # testing initializations
        result = len(self.match_robin.standings)
        self.assertEqual(result, 0)
        result = len(self.match_robin.teams)
        self.assertEqual(result, 0)
        # .update_standings() method call
        # test initializations
        self.match_robin.update_standings()
        result = len(self.match_robin.standings)
        self.assertEqual(result, 4)
        result = len(self.match_robin.teams)
        self.assertEqual(result, 4)
        # read data in from csv file
        # test initializations
        data = MatchReader("round_robin_matches.csv")
        new_robin = RoundRobin(161, matches=data.matches)
        result = len(new_robin.standings)
        self.assertEqual(result, 0)
        result = len(new_robin.teams)
        self.assertEqual(result, 0)
        # .update_standings() method call
        # test initializations
        new_robin.update_standings()
        result = len(new_robin.standings)
        self.assertEqual(result, 11)
        result = len(new_robin.teams)
        self.assertEqual(result, 11)
        # checking to make sure keys were not added to
        # game_stats nor tournament_stats
        for key in new_robin.teams:
            result = len(new_robin.teams[key].game_stats)
            self.assertEqual(result, 3)
            result = len(new_robin.teams[key].tournament_stats)
            self.assertEqual(result, 6)

    def test_update_standings_teams(self):
        # the teams in the teams attribute should be
        #  different team objects than the teams in matches
        data = MatchReader("round_robin_matches.csv")
        new_robin = RoundRobin(161, matches=data.matches)
        for match in new_robin.matches:
            team1 = match.team1
            team2 = match.team2
            for key in new_robin.teams:
                self.assertIsNot(team1, new_robin.teams[key])
                self.assertIsNot(team2, new_robin.teams[key])

    def test_update_standings_results(self):
        self.match_robin.update_standings()
        result = self.match_robin.standings
        expected_value = {
            "VT Hokies": 0,
            "UVA Wahoos": 2,
            "UNC Tar Heels": 2,
            "Duke Blue Devils": 2,
        }
        self.assertEqual(result, expected_value)

        data = MatchReader("round_robin_matches.csv")
        new_robin = RoundRobin(161, matches=data.matches)
        new_robin.update_standings()
        result = new_robin.standings
        expected_value = {
            "BC Eagles": 7,
            "Clemson Tigers": 6,
            "Creighton Bluejays": 4,
            "FSU Seminoles": 3,
            "GT YellowJackets": 4,
            "NC State Wolfpack": 2,
            "Pitt Panthers": 6,
            "Syracuse Orange": 7,
            "UNC TarHeels": 5,
            "UVA Cavaliers": 6,
            "VT Hokies": 5,
        }
        self.assertEqual(result, expected_value)

        # checking scores
        scores = [
            (74, 60),
            (81, 55),
            (67, 46),
            (75, 65),
            (71, 62),
            (79, 63),
            (79, 65),
            (73, 66),
            (55, 53),
            (71, 47),
            (65, 62),
            (72, 57),
            (51, 46),
            (62, 43),
            (81, 63),
            (61, 50),
            (60, 44),
            (80, 56),
            (53, 43),
            (64, 42),
            (51, 45),
            (61, 50),
            (73, 72),
            (67, 55),
            (70, 55),
            (60, 45),
            (62, 41),
            (79, 66),
            (61, 42),
            (67, 49),
            (56, 43),
            (64, 59),
            (78, 68),
            (55, 43),
            (64, 59),
            (64, 62),
            (78, 56),
            (74, 61),
            (62, 57),
            (53, 50),
            (82, 70),
            (67, 51),
            (67, 59),
            (82, 57),
            (78, 74),
            (55, 40),
            (66, 62),
            (63, 62),
            (55, 54),
            (63, 57),
            (77, 54),
            (62, 55),
            (58, 50),
            (62, 53),
            (78, 50),
        ]
        for index in range(len(scores)):
            scores[index] = sorted(scores[index])
        for m in new_robin.matches:
            self.assertIn(sorted(m.score), scores)
        scores = [(26, 24), (37, 16), (56, 18), (26, 19), (39, 32), (55, 45)]
        for index in range(len(scores)):
            scores[index] = sorted(scores[index])
        for m in self.match_robin.matches:
            self.assertIn(sorted(m.score), scores)

    def test_bracket_winner_not_completed(self):
        result = self.empty_robin.get_bracket_winner()
        self.assertEqual(len(result), 0)
        self.match_robin.update_standings()
        result = self.match_robin.get_bracket_winner()
        self.assertEqual(len(result), 3)

    def test_bracket_winner_completed(self):
        self.match_robin.update_standings()
        result = self.match_robin.get_bracket_winner()
        self.assertEqual(len(result), 3)

        # change a game to get 1 tournament winner
        team1 = self.match_robin.matches[5].team1
        for r in team1.roster:
            r.game_stats["points"] = 25
        team1.game_stats["points"] = 125
        self.match_robin.update_standings()
        standings = self.match_robin.standings
        standings["UNC Tar Heels"] += 1
        standings["Duke Blue Devils"] -= 1
        result = self.match_robin.get_bracket_winner()
        self.assertEqual(result[0].name, "UNC Tar Heels")

        # read in data
        # there are 2 teams with the most wins
        data = MatchReader("round_robin_matches.csv")
        new_robin = RoundRobin(161, matches=data.matches, status="completed")
        new_robin.update_standings()
        result = new_robin.get_bracket_winner()
        self.assertEqual(result[0].name, "Syracuse Orange")
        # change the game
        for match in new_robin.matches:
            if (
                match.team1.name == "Syracuse Orange"
                and match.team2.name == "BC Eagles"
            ):
                for p in match.team2.roster:
                    p.game_stats["points"] = 25
                match.team2.game_stats["points"] = 125
        result = new_robin.get_bracket_winner()
        self.assertEqual(result[0].name, "BC Eagles")


if __name__ == "__main__":
    unittest.main(verbosity=2)

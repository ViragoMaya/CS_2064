import unittest

from double_round_robin import DoubleRoundRobin
from team import Team


class TestDoubleRobin(unittest.TestCase):
    def test_generate_matches(self):
        """Test that the correct number of matches are generated"""
        team_a = Team("VT Hokies")
        team_b = Team("UVA Wahoos")
        team_c = Team("UNC Tar Heels")
        team_d = Team("Duke Blue Devils")
        teams = [team_a, team_b, team_c, team_d]

        self.double_robin = DoubleRoundRobin(1, participants=teams)
        self.double_robin.generate_matches()
        result = len(self.double_robin.matches)
        self.assertEqual(result, 12)
        teams.append(Team("NC State Wolfpack"))
        self.double_robin = DoubleRoundRobin(2, participants=teams)
        self.double_robin.generate_matches()
        result = len(self.double_robin.matches)
        self.assertEqual(result, 20)


if __name__ == "__main__":
    unittest.main(verbosity=2)

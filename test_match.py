"""Unit tests for the match class."""

import unittest

from match import Match
from team import Team


class TestMatch(unittest.TestCase):
    """Match tests covering constructor, __str__, and equality."""

    def setUp(self):
        """Set up common teams and a baseline match."""
        self.t1 = Team("VT Hokies")
        self.t2 = Team("UVA Cavaliers")
        self.m = Match(42, self.t1, self.t2)

    def test_constructor_defaults(self):
        """Verify constructor defaults are set correctly."""
        self.assertEqual(self.m.id, 42)
        self.assertIs(self.m.team1, self.t1)
        self.assertIs(self.m.team2, self.t2)
        self.assertEqual(self.m.status, "not started")
        self.assertEqual(self.m.score, (0, 0))

    def test_str(self):
        """Verify __str__ returns id : "status"' format."""
        self.m.status = "completed"
        self.assertEqual(str(self.m), '42 : "completed"')

    def test_eq_same_order(self):
        """Equal when id matches and teams are in the same order."""
        other = Match(42, Team("VT Hokies"), Team("UVA Cavaliers"))
        self.assertTrue(self.m == other)

    def test_eq_swap_order(self):
        """Equal when id matches even if team order is swapped."""
        other = Match(42, Team("UVA Cavaliers"), Team("VT Hokies"))
        self.assertTrue(self.m == other)

    def test_eq_different_id(self):
        """Not equal when ids differ."""
        other = Match(7, Team("VT Hokies"), Team("UVA Cavaliers"))
        self.assertFalse(self.m == other)

    def test_eq_different_teams(self):
        """Not equal when the set of teams differs."""
        other = Match(42, Team("UNC Tar Heels"), Team("UVA Cavaliers"))
        self.assertFalse(self.m == other)

    def test_id_non_numeric_fallback(self):
        """Keep non-numeric id as-is when int conversion fails."""
        a = Team("A")
        b = Team("B")
        m = Match("abc", a, b)
        self.assertEqual(m.id, "abc")

    def test_eq_non_match_type(self):
        """Return False when compared with a non-Match type."""
        self.assertFalse(self.m == "not a match")
        # coverage in isinstance guard in __eq__


if __name__ == "__main__":
    unittest.main(verbosity=2)

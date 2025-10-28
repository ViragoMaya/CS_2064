"""DoubleRoundRobin bracket system."""

from match import Match
from round_robin import RoundRobin


class DoubleRoundRobin(RoundRobin):
    """Double round robin: every team plays every other team twice."""

    def generate_matches(self):
        """Generate twice the unique pairings among participants and set status."""
        self.matches = []
        match_id = 1
        n = len(self.participants)
        for i in range(n):
            for j in range(i + 1, n):
                # First meeting
                self.matches.append(
                    Match(match_id, self.participants[i], self.participants[j])
                )
                match_id += 1
                # Second meeting (same pairing)
                self.matches.append(
                    Match(match_id, self.participants[i], self.participants[j])
                )
                match_id += 1
        self.status = "scheduled"

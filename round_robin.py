"""RoundRobin bracket implementation."""

from bracket import Bracket
from match import Match
from team import Team


class RoundRobin(Bracket):
    """Round robin tournament: every team plays every other team once."""

    def __init__(self, id, participants=None, status="not started", matches=None):
        """Initialize a RoundRobin bracket.

        Args:
            id (int|str): Bracket identifier.
            participants (list[Team]|None): Teams participating.
            status (str): Bracket status.
            matches (list[Match]|None): Pre-existing matches.

        """
        super().__init__(id, participants=participants, status=status, matches=matches)
        self.standings = {}
        self.teams = {}

    def __eq__(self, other):
        """Determine equality by bracket_id."""
        return isinstance(other, RoundRobin) and self.bracket_id == other.bracket_id

    def generate_matches(self):
        """Generate all unique pairings amongst participants and set status."""
        self.matches = []
        part_list = self.participants or []
        match_id = 1
        n = len(part_list)
        for i in range(n):
            for j in range(i + 1, n):
                self.matches.append(Match(match_id, part_list[i], part_list[j]))
                match_id += 1
        self.status = "scheduled"

    def _sum_stat(self, team_obj, key):
        """Compute team's single-match total for a given stat key (points).

        Prefer summing player game_stats if a roster is present; otherwise
        fallback to the team's game_stats for that match.
        """
        if getattr(team_obj, "roster", None):
            return sum(p.game_stats.get(key, 0) for p in team_obj.roster)
        return team_obj.game_stats.get(key, 0)

    def update_standings(self):
        """Update matches' scores, standings, and per-team tournament stats.

        Initialize standings + teams from match team names.
        Each match:
            Update match.score to games (team1_points, team2_points)
            Increment winning team's standing.
            Accumulate tournament stats in self.teams:
              points, rebounds, turnovers, wins, loses, number_of_games.
        """
        self.standings = {}
        self.teams = {}

        # If no matches, leave standings/teams empty.
        if not self.matches:
            return

        # Collect unique team names from matches.
        team_names = set()
        for m in self.matches:
            team_names.add(m.team1.name)
            team_names.add(m.team2.name)

        for name in team_names:
            self.standings[name] = 0
            self.teams[name] = Team(name)

        # Process each match.
        for m in self.matches:
            t1_name = m.team1.name
            t2_name = m.team2.name

            t1_pts = self._sum_stat(m.team1, "points")
            t2_pts = self._sum_stat(m.team2, "points")
            t1_rbs = self._sum_stat(m.team1, "rebounds")
            t2_rbs = self._sum_stat(m.team2, "rebounds")
            t1_tov = self._sum_stat(m.team1, "turnovers")
            t2_tov = self._sum_stat(m.team2, "turnovers")

            # Update match score.
            m.score = (t1_pts, t2_pts)

            # Determine winner for standings.
            winner_name = None
            loser_name = None
            if t1_pts > t2_pts:
                self.standings[t1_name] += 1
                winner_name, loser_name = t1_name, t2_name
            elif t2_pts > t1_pts:
                self.standings[t2_name] += 1
                winner_name, loser_name = t2_name, t1_name

            # Accumulate into unique team objects.
            t1 = self.teams[t1_name]
            t2 = self.teams[t2_name]

            # Team1 accumulation
            t1.tournament_stats["points"] += t1_pts
            t1.tournament_stats["rebounds"] += t1_rbs
            t1.tournament_stats["turnovers"] += t1_tov
            t1.tournament_stats["number_of_games"] += 1
            if winner_name == t1_name:
                t1.tournament_stats["wins"] += 1
            elif loser_name == t1_name:
                t1.tournament_stats["loses"] += 1

            # Team2 accumulation
            t2.tournament_stats["points"] += t2_pts
            t2.tournament_stats["rebounds"] += t2_rbs
            t2.tournament_stats["turnovers"] += t2_tov
            t2.tournament_stats["number_of_games"] += 1
            if winner_name == t2_name:
                t2.tournament_stats["wins"] += 1
            elif loser_name == t2_name:
                t2.tournament_stats["loses"] += 1

    def get_bracket_winner(self):
        """Return the winner(s) of the bracket per project rules.

        Returns:
             None if status != 'completed' or standings are empty.
             [team] if one team has the most wins.
             [team] if two teams tie, chosen by head-to-head match.
             [team_a, team_b] if tied two-team match not found.
             [tied teams...] if more than two teams tie.

        """
        if self.status != "completed":
            return None

        if not self.standings:
            return None

        max_wins = max(self.standings.values())
        tied = [name for name, w in self.standings.items() if w == max_wins]

        if len(tied) == 1:
            return [self.teams[tied[0]]]

        if len(tied) == 2:
            a, b = tied
            # Find their head-to-head match; compare per-match points.
            for m in self.matches or []:
                names = {m.team1.name, m.team2.name}
                if names == {a, b}:
                    a_pts = (
                        m.team1.game_stats["points"]
                        if m.team1.name == a
                        else m.team2.game_stats["points"]
                    )
                    b_pts = (
                        m.team1.game_stats["points"]
                        if m.team1.name == b
                        else m.team2.game_stats["points"]
                    )
                    winner = a if a_pts > b_pts else b
                    return [self.teams[winner]]
            # Fallback: both if match not found.
            return [self.teams[a], self.teams[b]]

        # > 2 tied: return all tied teams.
        return [self.teams[name] for name in tied]

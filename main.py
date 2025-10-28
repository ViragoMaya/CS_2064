"""Main program round robin program :
reads match data
process round robin
reports results
"""

from match_reader import MatchReader
from round_robin import RoundRobin


def main():
    """Run round robin analysis on csv match data using MatchReader"""
    # Reading matches from CSV
    data = MatchReader("round_robin_matches.csv")

    # building rr with such matches, marking as completed
    rr = RoundRobin(1, matches=data.matches, status="completed")

    # update standings and per team totals
    rr.update_standings()

    # determining winners and reporting
    winners = rr.get_bracket_winner()

    if not winners:
        print("No winner determined. Tournament bracket not completed.")
        return

    if len(winners) == 1:
        print(f"Round Robin Winner: {winners[0].name}")
    else:
        names = ", ".join(t.name for t in winners)
        print(f"Tie for Winner(s): {names}")

    # Analyzing two additional statistics.
    # A: Top-scoring team across the tournament.
    top_points_team = max(
        rr.teams.values(), key=lambda t: t.tournament_stats.get("points", 0)
    )
    print(
        f"Most total points: {top_points_team.name} "
        f"({top_points_team.tournament_stats['points']})"
    )

    # B: Fewest turnovers across the tournament.
    fewest_tov_team = min(
        rr.teams.values(), key=lambda t: t.tournament_stats.get("turnovers", 0)
    )
    print(
        f"Fewest total turnovers: {fewest_tov_team.name} "
        f"({fewest_tov_team.tournament_stats['turnovers']})"
    )


if __name__ == "__main__":
    main()

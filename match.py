"""Match model for the round robin tournament system."""


class Match:
    """Represents a match/contest between two teams.

    Attributes:
        id : (int) unique number for a Match object
        team1 :(Team) Team object
        team2 :(Team) Team object
        status : (str) not started, scheduled, completed

    """

    def __init__(self, id, team1, team2, status="not started"):
        """Initialize a Match.

        Args:
            id : (int) unique number for a Match object
            team1 :(Team) FirstTeam object
            team2 :(Team) Second Team object
            status : (str) not started, scheduled, completed

        """
        try:
            self.id = int(id)
        except (ValueError, TypeError):
            self.id = id
        self.team1 = team1
        self.team2 = team2
        self.status = status
        self.score = (0, 0)  # Default score

    def __str__(self):
        """Return a string of the form id: status."""
        return f"{self.id}: {self.status}"

    def __eq__(self, other):
        """Return True when ids match and teams match ignoring order."""
        if not isinstance(other, Match):
            return False
        if self.id != other.id:
            return False
        same = self.team1 == other.team1 and self.team2 == other.team2
        swapped = self.team1 == other.team2 and self.team2 == other.team1
        return same or swapped

"""Team class for round robin tournament system."""

from participant import Participant


class Team(Participant):
    """Team class representing group of players (via participant).

    Attributes:
        name (str): Team's name (school_name).
        status (str): Team's status, default 'active'.
        roster (list): List of Player objects.

    """

    def __init__(self, school_name, status="active", roster=None):
        """Initialize a Team object.

        Args:
            school_name (str): Team's school name.
            status (str): Team's status, default 'active'.
            roster (list): List of Player objects.

        """
        super().__init__(school_name, status)
        self.roster = roster if roster is not None else []
        self.tournament_stats["wins"] = 0
        self.tournament_stats["loses"] = 0

    def __str__(self):
        """Return string representation with winning percentage.

        Returns:
            str: team_name: winning_percent (2 decimals)

        """
        wins = self.tournament_stats.get("wins", 0)
        loses = self.tournament_stats.get("loses", 0)
        games = wins + loses
        if games == 0:
            percent = 0.00
        else:
            percent = round(wins / games, 2)
        return f"{self.name}: {percent:.2f}"

    def __eq__(self, other):
        """Check equality with another Team.

        Teams are equal if their names are equal.

        Args:
            other (Team): The object to compare.

        Returns:
            bool: True if equal, False otherwise.

        """
        return isinstance(other, Team) and self.name == other.name

    def get_tournament_stats(self):
        """Get a copy of the team's tournament stats, with winning_percent.

        Returns:
            dict: Copy of tournament stats with 'winning_percent' key.

        """
        stats = self.tournament_stats.copy()
        wins = stats.get("wins", 0)
        games = stats.get("number_of_games", 0)
        if games == 0:
            wp = 0.00
        else:
            wp = round(wins / games, 2)
        stats["winning_percent"] = wp
        return stats

    def get_player(self, name, number):
        """Get a player from the roster by name and number.

        Args:
            name (str): The player's name.
            number (int): The player's jersey number.

        Returns:
            Player or None: Returns Player if found, else None.

        """
        for player in self.roster:
            if player.name == name and player.number == number:
                return player
        return None

    def add_player(self, player):
        """Add a player to the team if not already present.

        Args:
            player (Player): Player object to add.

        Returns:
            bool: True if added, False if already exists.

        """
        for member in self.roster:
            if member.name == player.name and member.number == player.number:
                return False
        self.roster.append(player)
        return True

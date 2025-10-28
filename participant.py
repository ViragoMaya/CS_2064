from abc import ABC, abstractmethod


class Participant(ABC):
    def __init__(self, name, status):
        self.name = name
        self.status = status
        self.game_stats = {"points": 0, "rebounds": 0, "turnovers": 0}
        self.tournament_stats = {
            "points": 0,
            "rebounds": 0,
            "turnovers": 0,
            "number_of_games": 0,
        }

    def __str__(self):
        return f"{self.name}: {self.status}"

    def reset(self):
        self.game_stats = {"points": 0, "rebounds": 0, "turnovers": 0}

    def update_game_stats(self, points=0, rebounds=0, turnovers=0):
        self.update_tournament_stats(points, rebounds, turnovers)
        self.game_stats["points"] += points
        self.game_stats["rebounds"] += rebounds
        self.game_stats["turnovers"] += turnovers

    def update_tournament_stats(self, points=0, rebounds=0, turnovers=0):
        self.tournament_stats["points"] += points
        self.tournament_stats["rebounds"] += rebounds
        self.tournament_stats["turnovers"] += turnovers

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def get_tournament_stats(self):
        pass

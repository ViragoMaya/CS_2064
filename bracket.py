from abc import ABC, abstractmethod


class Bracket(ABC):
    def __init__(self, id, participants=None, status="not started", matches=None):
        self.bracket_id = id
        self.participants = participants
        self.matches = matches
        self.status = status

    def __str__(self):
        return f"{self.participants}"

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def generate_matches(self):
        pass

    @abstractmethod
    def get_bracket_winner(self):
        pass

    @abstractmethod
    def update_standings(self):
        pass

import csv

from match import Match
from player import Player
from team import Team


class MatchReader:
    def __init__(self, file_name):
        # teams is a dictionary
        # {team_name: Team object}
        self.matches = self.load_matches(file_name)

    def load_matches(self, file_name):
        matches = []
        match_by_teams = {}
        with open(file_name, newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                match_id = row["match id"]
                team_id = row["team name"]
                school = row["school"]
                player_number = int(row["player number"])
                player_name = row["player name"]
                points = int(row["points"])
                rebounds = int(row["rebounds"])
                turnovers = int(row["turnovers"])

                player = Player(player_name, player_number, school)
                player.game_stats["points"] = points
                player.game_stats["rebounds"] = rebounds
                player.game_stats["turnovers"] = turnovers

                if match_id not in match_by_teams:
                    match_by_teams[match_id] = {}

                if team_id not in match_by_teams[match_id]:
                    team = Team(team_id)
                    match_by_teams[match_id][team_id] = team
                else:
                    team = match_by_teams[match_id][team_id]

                team.add_player(player)
                team.game_stats["points"] += points
                team.game_stats["rebounds"] += rebounds
                team.game_stats["turnovers"] += turnovers

        for match_id in match_by_teams:
            team_list = list(match_by_teams[match_id].values())
            if len(team_list) == 2:
                temp_match = Match(match_id, team_list[0], team_list[1])
                score = [
                    team_list[0].game_stats["points"],
                    team_list[1].game_stats["points"],
                ]
                score.sort(reverse=True)
                temp_match.score = tuple(score)
                matches.append(temp_match)

        return matches

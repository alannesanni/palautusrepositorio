from statistics_service import StatisticsService
from player_reader import PlayerReader
from enumit import SortBy

def main():
    stats = StatisticsService(PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"))
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top point getters:")
    for player in top_scorers:
        print(player)

    print("Top goals:")
    top_goals=stats.top(10,SortBy.GOALS)
    for player in top_goals:
        print(player)

    print("Top assists:")
    top_assists=stats.top(10,SortBy.ASSISTS)
    for player in top_assists:
        print(player)


if __name__ == "__main__":
    main()

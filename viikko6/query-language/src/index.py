from statistics import Statistics
from player_reader import PlayerReader
from query import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi//nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder(stats)
    matcher = query.build()

    for player in stats.matches(matcher):
        print(player)

    
    
if __name__ == "__main__":
    main()

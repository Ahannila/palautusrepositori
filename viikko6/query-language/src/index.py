from statistics import Statistics
from player_reader import PlayerReader
from query_builder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi//nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = query.build()
    

    for player in stats.matches(matcher):
        print(player)

    #matcher = And(
    #    HasAtLeast(5, "goals"),z
    #    HasAtLeast(5, "assists"),
    #    PlaysIn("PHI")
    #)
    
    #matcher = And(
    #    HasFewerThan(1, "goals"),
    #    PlaysIn("NYR")
    #)

    #matcher = And(
    #    Not(HasAtLeast(1, "goals")),
    #    PlaysIn("NYR")
    #)

    #matcher = Or(
    #    HasAtLeast(45, "goals"),
    #    HasAtLeast(70, "assists")
    #)

    #matcher = And(
    #    HasAtLeast(70, "points"),
    #    Or(
    #        PlaysIn("NYR"),
    #        PlaysIn("FLA"),
    #        PlaysIn("BOS")
    #    )
    #)




if __name__ == "__main__":
    main()

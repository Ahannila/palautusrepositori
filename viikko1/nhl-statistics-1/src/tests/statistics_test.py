import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]



class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search(self):
        player1 = self.statistics.search("Semenko")
        player2 = Player("Semenko", "EDM", 4,12)

        self.assertEqual(player1.name, player2.name)

    def test_search_not_found(self):
        player1 = self.statistics.search("kekk")

        self.assertEqual(None, player1)
    
    def test_top_results(self):
        list = self.statistics.top(2)
        list2 = self.statistics.top(2)

        self.assertEqual(list,list2)

    def test_team_search(self):
        player1 = self.statistics.team("PIT")
        player2 = Player("Lemieux", "PIT", 45, 54)

        self.assertEqual(player1[0].name, player2.name)
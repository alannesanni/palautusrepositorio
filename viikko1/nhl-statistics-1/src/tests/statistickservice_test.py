import unittest
from statistics_service import StatisticsService
from player import Player
from enumit import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search(self):
        self.assertEqual(str(self.stats.search("Kurri")), "Kurri EDM 37 + 53 = 90" )

    def test_search_wrong_name(self):
        self.assertEqual(self.stats.search("Moi"), None )

    def test_team(self):
        self.assertEqual(str(self.stats.team("PIT")[0]), "Lemieux PIT 45 + 54 = 99")
        self.assertEqual(len(self.stats.team("PIT")), 1)

    def test_top(self):
        top_players=self.stats.top(3)
        self.assertEqual(str(top_players[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(len(self.stats.top(3)), 3)

    def test_top_points(self):
        top_players=self.stats.top(3, SortBy.POINTS)
        self.assertEqual(str(top_players[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(len(self.stats.top(3)), 3)

    def test_top_goals(self):
        top_players=self.stats.top(3, SortBy.GOALS)
        self.assertEqual(str(top_players[0]), "Lemieux PIT 45 + 54 = 99")
        self.assertEqual(len(self.stats.top(3)), 3)

    def test_top_assists(self):
        top_players=self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(str(top_players[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(len(self.stats.top(3)), 3)
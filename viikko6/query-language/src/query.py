from matchers import And, HasAtLeast, PlaysIn, All, HasFewerThan, Not, Or

class QueryBuilder:
    def __init__(self, stats):
        self.stats = stats

    def build(self):
        return self.stats
    
    def playsIn(self, team):
        pass

    def hasAtLeast(self, value, attr):
        pass
    def hasFewerThan(self, value, attr):
        pass
    
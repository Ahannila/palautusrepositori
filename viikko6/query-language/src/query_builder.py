from matchers import All, And, PlaysIn, HasAtLeast

class QueryBuilder:
    def __init__(self, query = All()):
        self._query = query

    def build(self):
        self._query.append(All())
        return matches

    

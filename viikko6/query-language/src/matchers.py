class And:
    def __init__(self, *matchers):  #Syntaksin avulla *matchers sisältää listan konstruktorille annetuista argumenteista
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class All:
    def __init__(self) -> None:
        pass
    
    def test(self):
        return True

class Not:
    def __init__(self, condition):
        self._cond = condition
    
    def test(self, player):
        return self._cond.test(player) is not True

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value

class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team

class Or:
    def __init__(self, *matches):
        self._matches = matches

    def test(self, player):
        for matcher in self._matches:
            if matcher.test(player):
                return True
        return False
class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

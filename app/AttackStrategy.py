import random
from abc import ABCMeta, abstractmethod


class AttackStrategy:
    __metaclass__ = ABCMeta

    @abstractmethod
    def select_squad(self, army):
        """A choice of a squad according to a strategy.

        Args:
            army: Army.
        """
        pass


class Random(AttackStrategy):
    """A random strategy."""

    def select_squad(self, army):
        """A choice of a squad in a random way.

        Args:
            army: Army.

        Returns:
            It returns a random squad.
        """
        squads = army.get_squads
        random_squad = random.randint(0, len(squads) - 1)
        return squads[random_squad]


class Weakest(AttackStrategy):
    """Strategy of attacking the weakest squad."""

    def select_squad(self, army):
        """A choice of the weakest squad.

        Args:
            army: Army.

        Returns:
            It returns the weakest squad.
        """
        res = None
        squads = army.get_squads
        min_experience = min([i.get_experience for i in squads])
        for i in squads:
            if i.get_experience == min_experience:
                res = i
                break
            else:
                res = None
        return res


class Strongest(AttackStrategy):
    """Strategy of attacking the strongest squad."""

    def select_squad(self, army):
        """A choice of the strongest squad.

        Args:
            army: Army.

        Returns:
            It returns the strongest squad.
        """
        res = None
        squads = army.get_squads
        max_experience = max([i.get_experience for i in squads])
        for i in squads:
            if i.get_experience == max_experience:
                res = i
                break
            else:
                res = None
        return res


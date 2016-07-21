from app import Squad
from app import AttackStrategy


class Army:
    """Armies consists of squads.

    Attributes:
        get_squads: It represents the squads list.

    """
    __squads = None
    __health = None
    __name_army = None

    def __init__(self, **kwargs):
        """Initialization armies names and a squads list."""
        self.__name_army = str(kwargs.pop('name'))
        self.__squads = [Squad.Squad(**kwargs)
                         for _ in range(1, kwargs.pop('squads')+1)]

    def get_health(self):
        """It represents the sum of squads' health.

        Returns:
            Armies health.
        """
        self.__health = sum([i.get_health for i in self.__squads])
        return self.__health

    def get_name(self):
        """It represents the army's name.

        Returns:
            Army's name.
        """
        return self.__name_army

    @property
    def get_squads(self):
        return self.__squads

    def attack(self, army, strategy):
        """The attack success probability of a squad is determined
        as the arithmetic average of the attack success probability
        squads.

        Args:
            army: Army.
            strategy: Strategy of squad choice.
        """
        damage = sum([i.do_attack for i in self.__squads]) / len(self.__squads)
        if damage > 0:
            army.take_damage(damage, strategy, army)

    @staticmethod
    def take_damage(damage, strategy_name, army):
        """A choice of a squad according to a strategy and causing damage.

        Args:
            damage: Damage, the soldiers will receive.
            strategy_name: A name of a strategy.
            army: Army.
        """
        if strategy_name == 'random':
            strategy_ = AttackStrategy.Random()
        elif strategy_name == 'weakest':
            strategy_ = AttackStrategy.Weakest()
        else:
            strategy_ = AttackStrategy.Strongest()
        squad = strategy_.select_squad(army)
        squad.take_damage(damage)


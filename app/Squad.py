from app import Units


class Squad:
    """Squads are consisted out of a number of units (soldiers or vehicles),
    that behave as a coherent group.
    A squad is active as long as is contains an active unit.

    Attributes:
        get_experience: It represents the sum of soldiers' experience.
        get_health: It represents the sum of units' health.
        do_attack: The attack success probability of a squad is determined
        as the arithmetic average of the attack success probability of
        each member.
    """
    __units = None
    __health = None

    def __init__(self, **kwargs):
        """Initialization of a units list that consists of soldiers and
        vehicles"""
        self.__units = [Units.Solder() for _ in range(1, kwargs['soldiers']+1)]
        self.__units += [Units.Vehicles() for _ in range(1, kwargs['vehicles']+1)]

    @property
    def get_units(self):
        return self.__units

    @property
    def get_experience(self):
        return sum([i.get_experience for i in self.__units])

    @property
    def get_health(self):
        self.__health = sum([i.get_health for i in self.__units])
        return self.__health

    @property
    def do_attack(self):
        return sum([i.do_attack for i in self.__units]) / len(self.__units)

    def take_damage(self, damage):
        """Calculation the damage amount of a squad. The damage received
        on a successful attack is distributed evenly to all squad members.

        Args:
            damage: Damage, the squad will receive.
        """
        damage /= len(self.__units)
        for i in self.__units:
            i.take_damage(damage)


import random
import time
from abc import ABCMeta, abstractmethod, abstractproperty


class Unit:
    """Each unit represents either a soldier or a vehicle maned
    by a predetermined number of soldiers.

    Attributes:
        prev_time: Time of the previous attack.
        get_health: Represents the health of the unit.
        get_recharge: Represents the number of ms required to recharge
        the unit for an attack.
        get_experience: Represents the soldier's experience.
        do_attack: It calculates a probability of units' attack success.
        It increases soldiers' experience and reduces health.
        It returns soldiers' attack.
    """
    __metaclass__ = ABCMeta
    __health = None
    __recharge = None
    # __next_attack_time = 0
    prev_time = None

    @abstractproperty
    def do_attack(self):
        pass

    @abstractmethod
    def take_damage(self, damage):
        pass

    @property
    def get_recharge(self):
        return self.__recharge

    def set_recharge(self, recharge):
        """Set recharge of Units.

        Args:
            recharge: The recharge of the unit.
        """
        self.__recharge = recharge

    @property
    def get_health(self):
        return self.__health

    def set_health(self, health):
        """Set health of Units.

        Args:
            health: The health of the unit.
        """
        self.__health = health

    @abstractproperty
    def get_experience(self):
        pass

    """
    @property
    def get_next_attack_time(self):
        return self.__next_attack_time

    def set_next_attack_time(self, next_attack_time):
        self.__next_attack_time = next_attack_time
    """

    def check_attack(self):
        """Checking for the possibility of committing the attack.
        It compares the current time and the next attack time.

        Returns:
            It returns True if the attack is possible or False if recharging
            has not passed yet.
        """
        now = time.time() * 1000
        if self.prev_time is None:
            return True
        else:
            next_time = self.prev_time + self.get_recharge
            if now >= next_time:
                return True
            else:
                return False


class Solder(Unit):
    """Soldiers are units whose additional property is experience.

    This class calculates probability of soldiers' attack success
    and the complete damage.

    Attributes:
        get_experience: It represents the soldiers' experience.
        do_attack: It calculates a probability of soldiers' attack success.
        It increases soldiers' experience. It returns soldiers' attack.
    """
    __experience = 0

    def __init__(self):
        """Initialization of a soldier's health and recharge."""
        self.set_health(100)
        self.set_recharge(random.randint(100, 2000) / 10000)

    @property
    def get_experience(self):
        return self.__experience

    def set_experience(self):
        """Set experience of a Soldier. Maximum of 50."""
        if self.__experience < 50:
            self.__experience += 1

    @property
    def do_attack(self):
        if self.get_health > 0 and self.check_attack():
            soldiers_attack = 0.5 * (1 + self.get_health) * \
                random.randint(50 + self.__experience, 100) / 100
            self.set_experience()
            self.prev_time = time.time() * 1000
            return soldiers_attack
        else:
            return 0

    def take_damage(self, damage):
        """Calculation the damage amount of a soldier and reducing
        the soldier's health.

        Args:
            damage: Damage, the soldiers will receive.
        """
        attack = damage - (0.05 + self.__experience / 1000)
        self.set_health(self.get_health - attack)


class Vehicles(Unit):
    """Vehicles are units whose additional property is operators quantity.

    This class calculates probability of vehicles attack success
    and the complete damage.

    Attributes:
        operators: It represents the operators list.
        get_experience: It represents the sum of soldiers' experience.
        do_attack: It calculates a probability of vehicles' attack success.
        It returns vehicles' attack.
    """
    operators = []

    def __init__(self):
        """Initialization of a vehicles recharge and operators quantity.
        Creating of an operators list. And vehicles health calculation."""
        self.set_recharge(random.randint(1000, 2000) / 10000)
        operator_count = random.randint(1, 3)
        self.operators = [Solder() for _ in range(0, operator_count)]
        list_operators = [i.get_health for i in self.operators]
        self.set_health(sum(list_operators) / len(list_operators))

    def get_operators(self):
        return self.operators

    @property
    def get_experience(self):
        return sum([i.get_experience for i in self.operators])

    @staticmethod
    def alive(units):
        """It shows are there at least one soldier alive.

        Args:
            units: The list of soldiers.

        Returns:
            True if at least one soldier alive otherwise False.
        """
        res = False
        for i in units:
            if i.get_health > 0:
                res = True
                break
        return res

    @property
    def do_attack(self):
        if self.get_health > 0 and self.check_attack() \
                and self.alive(self.operators):
            list_attack_soldiers = [i.do_attack for i in
                                    self.operators]
            vehicles_attack = 0.5 * (1 + self.get_health / 100) * (
                sum(list_attack_soldiers) / len(list_attack_soldiers))
            self.prev_time = time.time() * 1000
            return vehicles_attack
        else:
            return 0

    def take_damage(self, damage):
        """Calculation the damage amount of a vehicle and reducing
        the vehicle and soldiers health. 60% of damage will receive a vehicle,
        20 % of damage will receive a random operator and the remaining
        will receive 10%.

        Args:
            damage: Damage, the vehicles will receive.
        """
        list_operators_experience = [i.get_experience / 1000 for i in
                                     self.operators]
        damage -= 0.1 + sum(list_operators_experience)
        # 60% of damage will receive a vehicle
        self.set_health(self.get_health - damage * 0.6)
        # A random operator, who will receive 20% of damage.
        random_operator = random.randint(0, len(self.operators) - 1)
        j = 0
        while j < len(self.operators):
            if j == random_operator:
                self.operators[j].take_damage(damage * 0.2)
            else:
                self.operators[j].take_damage(damage * 0.1)
            j += 1


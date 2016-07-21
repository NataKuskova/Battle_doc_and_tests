import pytest
from app import AttackStrategy
from app.Army import Army
from app.Squad import Squad


def test_random():
    rand = AttackStrategy.Random()
    army = Army(squads=3, soldiers=5, vehicles=4, name=1)
    assert isinstance(rand.select_squad(army), Squad)


def test_weakest():
    weakest = AttackStrategy.Weakest()
    army = Army(squads=3, soldiers=5, vehicles=4, name=1)
    assert isinstance(weakest.select_squad(army), Squad)


def test_strongest():
    strongest = AttackStrategy.Strongest()
    army = Army(squads=3, soldiers=5, vehicles=4, name=1)
    assert isinstance(strongest.select_squad(army), Squad)


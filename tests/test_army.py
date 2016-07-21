from app.Army import Army


def test_squads():
    army = Army(squads=3, soldiers=5, vehicles=4, name=1)
    assert len(army.get_squads) == 3


def test_health():
    army = Army(squads=3, soldiers=5, vehicles=4, name=1)
    army2 = Army(squads=5, soldiers=3, vehicles=6, name=2)
    i = 0
    while i <= 100:
        army.attack(army2, 'random')
        i += 1
    assert type(army2.get_health()) == float

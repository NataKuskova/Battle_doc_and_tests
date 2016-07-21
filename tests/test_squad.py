from app.Squad import Squad


def test_units():
    squad = Squad(soldiers=5, vehicles=3)
    assert len(squad.get_units) == 8


def test_experience_type():
    squad = Squad(soldiers=5, vehicles=3)
    assert type(squad.get_experience) == int


def test_do_attack_type():
    squad = Squad(soldiers=5, vehicles=3)
    assert type(squad.do_attack) == float


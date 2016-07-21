from app import Units


def test_do_attack():
    solder = Units.Solder()
    solder.set_health(70)
    assert solder.do_attack >= 0


def test_health_soldiers():
    solder = Units.Solder()
    solder.set_health(70)
    i = 0
    while i <= 100:
        solder.take_damage(solder.do_attack)
        i += 1
    assert solder.get_health <= 100


def test_health_vehicles():
    vehicle = Units.Vehicles()
    vehicle.set_health(70)
    i = 0
    while i <= 100:
        vehicle.take_damage(vehicle.do_attack)
        i += 1
    assert vehicle.get_health <= 100


def test_experience():
    solder = Units.Solder()
    solder.set_health(100)
    i = 0
    while i <= 400:
        solder.take_damage(solder.do_attack)
        i += 1
    assert 0 <= solder.get_experience <= 50


def test_do_attack_type_solder():
    solder = Units.Solder()
    assert type(solder.do_attack) == float


def test_do_attack_type_vehicle():
    vehicle = Units.Vehicles()
    assert type(vehicle.do_attack) == float


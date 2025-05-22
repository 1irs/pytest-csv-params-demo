import pytest

from uut import calculate_traffic_fine


@pytest.mark.parametrize(
    "speed,limit,zone,license_points,expected,msg",
    [
        (50, 50, "residential", 0, 0, "Нема перевищення швидкості"),
        (51, 50, "highway", 0, 50, "Мінімальне перевищення"),
        (51, 50, "school", 0, 100, "Біля школи коеф. 2х"),
        # ...
        # Ще 10 таких прикладів.
    ]
)
def test_calculate_traffic_fine(speed, limit, zone, license_points, expected, msg):
    assert calculate_traffic_fine(speed, limit, zone, license_points) == expected, msg

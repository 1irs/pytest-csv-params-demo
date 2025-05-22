from uut import calculate_traffic_fine


def test_no_fine():
    assert calculate_traffic_fine(50, 50, "residential", 0) == 0, "Нема перевищення швидкості"

def test_minimum_fine():
    assert calculate_traffic_fine(51, 50, "highway", 0) == 50, "Мінімальне перевищення"

def test_school_area():
    assert calculate_traffic_fine(51, 50, "school", 0) == 100, "Біля школи коеф. 2х"

from pytest_csv_params.decorator import csv_params

from uut import calculate_traffic_fine


@csv_params(
    data_file="calculate_traffic_fine_tests.csv",
    data_casts={
        "speed": int, "limit": int, "license_points": int, "expected": int,
    },
)
def test_calculate_traffic_fine(speed, limit, zone, license_points, expected, msg):
    assert calculate_traffic_fine(speed, limit, zone, license_points) == expected, msg

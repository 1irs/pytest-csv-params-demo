# Traffic Fine Calculator — Pytest CSV Demo

This project demonstrates how to write clean, scalable, and maintainable automated tests using `pytest-csv-params`, a plugin that allows loading test cases from CSV files.

The core example is a function that calculates traffic fines based on speeding severity, zone type, and driver penalty points.

## Project Structure

```
.
├── calculate_traffic_fine_tests.csv      # Test data in CSV format
├── test_csv_params.py                    # Main test file using pytest-csv-params
├── test_params.py                        # Classic pytest.mark.parametrize example
├── test_simple.py                        # One-test-per-function approach
├── uut.py                                # Function under test (calculate_traffic_fine)
```

## Function Under Test

The function `calculate_traffic_fine()` computes fines based on:

- Degree of speeding
- Type of zone (residential, school, highway, construction)
- Driver's license points

Defined in `uut.py`.

## Testing Approaches

This repo demonstrates three ways to structure test data:

| File | Strategy |
|------|----------|
| test_simple.py | One test function per case (not scalable) |
| test_params.py | `@pytest.mark.parametrize` with inline data |
| test_csv_params.py | `@csv_params` loading from external CSV (recommended) |

## CSV-Based Testing Example

The file `calculate_traffic_fine_tests.csv` contains test rows like:

```csv
speed,limit,zone,license_points,expected,msg
50,50,residential,0,0,No speeding
51,50,highway,0,50,Minimal speeding
51,50,school,0,100,Near school, 2x multiplier
51,50,highway,1,75,Repeat violation
```

These values are loaded dynamically into tests using:

```python
from pytest_csv_params.decorator import csv_params

@csv_params(
    data_file="calculate_traffic_fine_tests.csv",
    data_casts={
        "speed": int, "limit": int, "license_points": int, "expected": int,
    },
)
def test_calculate_traffic_fine(speed, limit, zone, license_points, expected, msg):
    from uut import calculate_traffic_fine
    assert calculate_traffic_fine(speed, limit, zone, license_points) == expected, msg
```

## Quick Start

1. Clone the repo:

   ```bash
   git clone https://github.com/your-username/traffic-fine-csv-demo
   cd traffic-fine-csv-demo
   ```

2. Install dependencies:

   ```bash
   pip install pytest pytest-csv-params
   ```

3. Run tests:

   ```bash
   pytest
   ```

## Dependencies

- Python 3.7+
- pytest
- pytest-csv-params

## License

This project is released under the MIT License.

## Credits

Created for educational and demonstration purposes as illustration to the blog posts:

* https://first.institute/blog/vidokremyty-dani-vid-kodu-testuvannya-z-csv-pytest/

def calculate_traffic_fine(speed: int, limit: int, zone: str, license_points: int) -> int:
    """
    Calculates the traffic fine based on speed, speed limit, zone type, and driver license points.

    Parameters:
        speed (int): Vehicle speed.
        limit (int): Legal speed limit.
        zone (str): Type of zone (residential, school, highway, construction).
        license_points (int): Number of penalty points the driver has.

    Returns:
        int: Amount of the fine in dollars.
    """
    over_speed = speed - limit
    base_fine = 0

    if over_speed <= 0:
        # No speeding — no fine applied
        return 0

    # Base fine tiers
    if over_speed <= 10:
        base_fine = 50
    elif over_speed <= 20:
        base_fine = 100
    else:
        base_fine = 200

    # Fine multipliers for different zone types
    zone_multipliers = {
        'residential': 1.5,  # residential area
        'school': 2.0,  # school area
        'construction': 2.5,  # construction zone
        'highway': 1.0,  # highway
    }

    multiplier = zone_multipliers.get(zone.lower(), 1.0)

    # Additional penalty based on license points
    penalty = 25 * license_points

    total_fine = int(base_fine * multiplier + penalty)
    return total_fine

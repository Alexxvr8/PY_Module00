""" Module for tracking seed inventory by unit type """


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    """Print seed inventory information based on the given unit."""
    seed_type = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed_type} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type} seeds: cover {quantity} square meters")
    else:
        print("Unknown unit type")

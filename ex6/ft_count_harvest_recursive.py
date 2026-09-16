""" Module to count up to harvest day using a recursive function """


def ft_count_harvest_recursive(current: int = 1, total: int = None) -> None:
    """ increment days to harvest day """
    if total is None:
        total = int(input("Days until harvest: "))
    if current <= total:
        print(f"Day {current}")
        ft_count_harvest_recursive(current + 1, total)
    else:
        print("Harvest time!")

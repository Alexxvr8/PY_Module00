""" Module to count up to harvest day using an iterative function """


def ft_count_harvest_iterative() -> None:
    """ increment days to harvest day """
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")

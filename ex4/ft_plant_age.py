""" Module to tell if a plant is growing """


def ft_plant_age() -> None:
    """ Ask the age and tell if it is ready to harvest """
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")

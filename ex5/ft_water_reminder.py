""" Module to know if the plants need water """


def ft_water_reminder() -> None:
    """ Ask days and tell if it needs water """
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")

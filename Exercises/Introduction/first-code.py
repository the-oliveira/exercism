"""
    This Module calculates the time to make your lasagna, the time that already bake, and elapsed time to be ready.
"""
EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    expected_time = EXPECTED_BAKE_TIME
    time_remaining = expected_time - elapsed_bake_time
    return time_remaining


def preparation_time_in_minutes(number_of_layers):
    """Calculate the prapration time to make your lasagna.

    :param number_of_layers: int - The number of layers of the lasagna.
    :return: int - The time (in minutes) to make the lasagna based on the number of
    layers.

    Function that calculate the time to make the lasagna based in the number of layers.       (assuming that each layer takes 2 minutes)
    """
    preparation_time = number_of_layers * 2
    return preparation_time


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time for your lasagna be ready based in the time that the        lasagna already spent baking and the number of layers.

    :param elapsed_bake_time int - The time already spent baking.
    :param number_of_layers: int - The number of layers of the lasagna.
    :return: int - The time (in minutes) left to your lasagna be ready.
    """
    elapsed_time = (number_of_layers * 2) + elapsed_bake_time
    return elapsed_time
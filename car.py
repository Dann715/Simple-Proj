import math
class Car:
    """
    A class representing a car with different attributes

    Attributes are:
    x : The x coordinate of the car.
    y : The y coordinate of the car.
    heading: The heading of the car in degrees.
    By default these are all 0 for now.
    """

#initialization
    def __init__(self, x=0.0, y=0.0, heading=0.0):
        """
        Initializes a new instance of the Car class.

        Arguments are the same as docstring above
        """
        self.x = x
        self.y = y
        self.heading = heading

#turning the cars function
    def turn(self, degrees):
        """
        Turn the car by a specified number of degrees.

        Arguments:
        degrees: The number of degrees to turn. Positive for clockwise and negative for counterclockwise.

        Returns:
        None
        """
        self.heading = (self.heading + degrees) % 360

#drive function
    def drive(self, distance):
        """
        Drive the car forward by a specific distance.

        Arguments:
        distance: The distance to drive.

        Returns:
        None
        """
        radians_heading = math.radians(self.heading)
        self.x += distance * math.sin(radians_heading)
        self.y -= distance * math.cos(radians_heading)



def sanity_check():
    """
    Perform a sanity check by creating an instance of the Car class, making turns, and driving distances.
    This also prints the location and heading of the car.

    Returns:
    Car: The instance of the Car class
    """
    car_instance = Car()
    car_instance.turn(90)
    car_instance.drive(10)
    car_instance.turn(30)
    car_instance.drive(20)

    print(f"Location: {car_instance.x}, {car_instance.y}")
    print(f"Heading: {car_instance.heading}")

    return car_instance


if __name__ == "__main__":
    sanity_check()

class Car:
    """
    A class representing a car.

    :param color: the color of the car
    :param model: the model of the car
    :param make: the make of the car
    :attr color: the color of the car
    :attr speed: the speed of the car
    :attr model: the model of the car
    :attr make: the make of the car
    :attr parked: whether the car is parked or not
    """

    def __init__(self, color: str, model: str, make: str):
        """
        Initialize a car with color, model and make

        :param color:
        :param model:
        :param make:
        """
        self.color = color
        self.speed = 0
        self.model = model
        self.make = make
        self.parked = True

    def speed_up(self, s: int) -> None:
        """
        Accelerate the car by s

        :param s:
        :return:
        """
        if s > 0:
            self.speed += s
            self.parked = False

    def slowing_down(self, q: int) -> None:
        """
        decelerate the car by q
        Precondition: q > 0

        :param q:
        :return:
        """
        if q > 0:
            self.speed -= q
            if self.speed < 0:
                self.speed = 0
            if self.speed == 0:
                self.parked = True

    def stop(self) -> None:
        """
        Stop the car

        :return:
        """
        self.speed = 0
        self.parked = True


b = Car('Red', '2023', 'BMW')

print(b.color)
print(b.make)
print(b.parked)
print(b.speed)
b.speed_up(10)
print(b.speed)
print(b.parked)
b.stop()
print(b.parked)
print(b.speed)

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 24
    
    def get_descripitive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it")
    
    def update_odometer(self, mileage):
        """
        Set the odometer eading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

#were leveraging the Car class above and passing it values. 
my_new_car = Car('toyota', 'rav4', 2019)
print(my_new_car.get_descripitive_name())
#were overiding the default value of the odometer
my_new_car.update_odometer(23)
#its going to print out the odometer reading
my_new_car.read_odometer()
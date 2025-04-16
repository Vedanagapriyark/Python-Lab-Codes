from datetime import datetime

class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year

    def get_age(self):
        current_year = datetime.now().year
        return current_year - self.year

# Example usage
if __name__ == "__main__":
    my_car = Car("Toyota", "Camry", 2015)
    print(f"My car is a {my_car.company} {my_car.model} from {my_car.year}.")
    print(f"It is {my_car.get_age()} years old.")

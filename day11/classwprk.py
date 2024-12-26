from datetime import datetime

class FindAge:
    def _init_(self, country, name, age):
        assert age > 0, "please enter your age grater than 0"
        self.date = datetime.now().date()
        self.current_year = datetime.now().year
        self.country = country
        self.name = name
        self.age = age

    def calculate_year(self):
        year_of_birth = self.current_year - self.age
        return year_of_birth

    def display_details(self):
        year_of_birth = self.calculate_year()
        print(f"Hello, {self.name} from {self.country}!")
        print(f"You are {self.age} years old as of {self.date}.")
        print(f"Based on your age, you were likely born in {year_of_birth}.")

country = input("Enter your country: ")
name = input("Enter your name: ")
age = int(input("Enter your age: "))

person = FindAge(country, name, age)

person.display_details()
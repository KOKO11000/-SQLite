import sqlite3
class Person:
    def __init__(self,person_id, name, age, email):
        self.person_id:int = person_id  
        self.name: str = name
        self.age: int = age
        self.email: str = email
        self.cars: list = []

    def add_car(self):
        self.cars.append()
        return self.cars

    def get_cars_count(self):
        count_cars = self.cars
        return len(count_cars)
    
    def __str__(self):
        print(f"Hello {self.name} your age is {self.age} and your email {self.email} your id {self.person_id} you have a {self.get_cars_count()} cars your own")

    def to_dict(self):
        convetion_to_dict = {"person_id":self.person_id,"name":self.name,"age":self.age,"email":self.email,"cars":self.get_cars_count()}
        return convetion_to_dict



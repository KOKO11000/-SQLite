from datetime import datetime
class Car:
    def __init__(self, car_id, brand, model, year, color, owner_id = None):
        self.car_id: int = car_id
        self.brand: str = brand
        self.model: str = model
        self.year: int = year
        self.color: str = color
        self.owner_id: int = owner_id

    def __str__(self):
        print(f"you have a {self.brand} \nmodel: {self.model} \nyear: {self.year} \ncolor: {self.color} \nid car: {self.car_id} \nowner_id: {self.owner_id}")

    def to_dict(self):
        return {"car id" :self.car_id, "brand": self.brand, "model": self.model, "year":self.year,"color":self.color,"owner_id": self.owner_id} 

    def get_age(self):        
        year = datetime.today().year
        car_age = year - self.year
        return car_age

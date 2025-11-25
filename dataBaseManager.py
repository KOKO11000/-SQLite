import sqlite3

class DataBaseManager:
    def __init__(self, db_name = "persons_cars.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def creat_tables(self):
        pass

    def insert_person(self):
        pass

    def insert_car(self):
        pass

    def get_all_persons(self):
        pass

    def get_all_cars(self):
        pass

    def get_person_by_id(self, person_id):
        pass

    def get_car_by_owner(self, owner_id):
        pass

    def update_person(self, person):
        pass

    def delete_person(self, person_id):
        pass

    def close(self):
        self.connection.close()
import sqlite3
from person import Person
from car import Car
class DataBaseManager:
    def __init__(self, db_name = "persons_cars.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def creat_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS person (                                   
                person_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age  INTEGER NOT NULL,
                email TEXT UNIQUE NOT NULL)
            """)
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS car(
                                   
                car_id INTEGER primary key,
                brand TEXT NOT NULL,
                model TEXT NOT NULL, 
                year INTEGER NOT NULL,
                color TEXT NOT NULL,
                owner_id INTEGER,
                FOREIGN KEY (owner_id) REFERENCES person(person_id))                                                                                         
            """)
        self.connection.commit()
        

    def insert_person(self):
        ins_person = self.cursor.execute(
            "INSERT INTO person(" 
            "VALUES)", "?,?,?,?"
        )
        return ins_person

    def insert_car(self):
        ins_car = self.cursor.execute(
            "INSERT INTO car(" 
            "VALUES)", "?,?,?,?"
        )
        return ins_car


    def get_all_persons(self):
        select_person = self.cursor.execute("select * from person")
        return select_person

    def get_all_cars(self):
        select_car = self.cursor.execute("select * from car")
        return select_car


    def get_person_by_id(self, person_id):
        get_person_id = self.cursor.execute(f"SELECT * FORM person WHERE {person_id}")
        return get_person_id

    def get_car_by_owner(self, owner_id):
        get_car_id = self.cursor.execute(f"SELECT * FORM car WHERE {owner_id}")
        return get_car_id

    def update_person(self, person, result):
        update = self.cursor.execute(f"UPDATE person SET {person} = {result}")
        return update

    def delete_person(self, person_id):
        delete = self.cursor.execute(f"DELETE FROM person WHERE {person_id}")
        return "The person deleted succsfully!"

    def close(self):
        self.connection.close()

a = DataBaseManager()
a.creat_tables()
""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self, brand, modle, year):#contructor method ของแม่
        self.brand = brand
        self.modle = modle
        self.year  = year
       
    def get_info(self):
        return f"Brand: {self.brand}, model: {self.model}, Year:{self.year}"    
 
class Car(Vehicle):# คลาส Car รับถ่ายทอดจากคลาส Vehicle
 
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
 
    def get_info(self):
        return f"Brand: {self.modle}, Year: {self.year}, Number of doors: {self.number_of_doors}"  
 
MyCar = Car("Toyota", "Yaris Cross", 2025, 4)
print(MyCar.get_info)
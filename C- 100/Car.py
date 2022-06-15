class Car:
    def __init__ (self,name,brand,material,color,speed_limit):
        self.name = name
        self.brand = brand
        self.material = material
        self.color = color
        self.speed_limit = speed_limit
    
    def start(self):
        print ("car started")
    
    def stop(self):
        print("car stoped")

    def acceleration(self):
        print("accelerating")
    
    def gear_change(self,gear_type):
        print("the gear has been changed to ",gear_type)

car1 = Car("audi A6", "audi", "aluminium", "black",220)

car1.start()
car1.gear_change(3)
car1.stop()
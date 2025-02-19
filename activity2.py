#create class
class Vehicle:


    #create init method
    def __init__(self, max_speed, mileage):
        

        #bind the arguments
        self.max_speed = max_speed
        self.mileage = mileage


#object creation
modleX = Vehicle(240, 18)


#access the variables inside init method
print("Model Max Speed:",modleX.max_speed)
print("Model Mileage:", modleX.mileage)
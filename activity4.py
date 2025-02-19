class Dog:
    animal = "dog"

    
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color


dog1 = Dog("Labrador", "Black")
dog2 = Dog("Beagle", "Brown")

print("Breed:", dog1.breed)
print("Color:", dog1.color)

print("{} is {} in color".format( dog1.breed, dog1.color))
print("{} is {} in color".format( dog2.breed, dog2.color))
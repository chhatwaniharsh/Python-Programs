class Honda:
    def max_speed(self):
        print("Max Speed of Honda is 220 KMPH")
    def transmission(self):
        print("Transmission of Honda is Manual")
    def fuel_type(self):
        print("Fuel Type of Honda is DISEL")

class Skoda:
    def max_speed(self):
        print("Max Speed of Skoda is 280 KMPH")
    def transmission(self):
        print("Transmission of Skoda is Automatic")
    def fuel_type(self):
        print("Fuel Type of Skoda is PETROL")

def get_info(obj):
    obj.max_speed()
    obj.transmission()
    obj.fuel_type()
    print()

honda_city=Honda()
skoda_slavia=Skoda()
get_info(honda_city)
get_info(skoda_slavia)

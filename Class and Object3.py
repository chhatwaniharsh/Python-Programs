class Laptop:
    brand="Lenovo"
    model="LOQ"
    RAM=24
    ROM=512
    price=70000.0

l1=Laptop()
print(l1)
print(l1.brand)
print(l1.model)
print(l1.RAM)
l1.RAM=32
print(l1.RAM)
print(l1.ROM)
print(l1.price)

print()

l2=Laptop()
l2.brand="Asus"
l2.model="Tuf F15"
l2.RAM=12
l2.ROM=256
l2.price=62000
print(l2.brand)
print(l2.model)
print(l2.RAM)
print(l2.ROM)
print(l2.price)

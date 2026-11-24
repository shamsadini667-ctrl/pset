def enistien(mass):
    c = 300000000
    m = mass
    e = m * c**2
    return e


try:
    mass = int(input("enter mass (kilograms):"))

    if mass < 1:
        print("mass cannot be negative.")
    else:
        energy = enistien(mass)
        print(energy)

except ValueError:
    print("enter a valid number.")
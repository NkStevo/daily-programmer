import math

gravitational_constant = 6.67 * 10 ** -11

def gravitional_force():
    global gravitational_constant

    try:
        mass_1 = float(input("Input the mass of the first object (kilograms)\n"))
        mass_2 = float(input("Input the mass of the second object (kilograms)\n"))
        distance = float(input("Input the distance between the two objects (meters)\n"))
    except:
        print("Invalid entry!")
        return -1

    return gravitational_constant * mass_1 * mass_2 / distance ** 2

def distance_between_objects():
    global gravitational_constant

    try:
        mass_1 = float(input("Input the mass of the first object (kilograms)\n"))
        mass_2 = float(input("Input the mass of the second object (kilograms)\n"))
        force = float(input("Input the gravitational force between the two objects (newtons)\n"))
    except:
        print("Invalid entry!")
        return -1

    return math.sqrt(gravitational_constant * mass_1 * mass_2 / force)

def mass_of_object():
    global gravitational_constant

    try:
        mass = float(input("Input the mass of the known object (kilograms)\n"))
        force = float(input("Input the gravitational force between the two objects (newtons)\n"))
        distance = float(input("Input the distance between the two objects (meters)\n"))
    except:
        print("Invalid entry!")
        return -1

    return force * distance ** 2 / gravitational_constant * mass

def main():
    print("Input 1 to find the gravitational force between two objects given their masses and the distance between them")
    print("Input 2 to find the distance between two objects given their masses and the gravitational force between them")
    print("Input 3 to find the mass of an object given the mass of another object and the distance and gravitational force between the two")

    option = input()

    if option == "1":
        print(str(gravitional_force()))
    elif option == "2":
        print(str(distance_between_objects()))
    elif option == "3":
        print(str(mass_of_object()))
    else:
        print("Invalid entry!")


if __name__ == '__main__':
    main()

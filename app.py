# introducerea coordonatelor patratului
while True:
    x_coord = int(input("Introduceti coordonata x_coord (10-50): "))
    y_coord = int(input("Introduceti coordonata y_coord (10-50): "))
    if 10 <= x_coord <= 50 and 10 <= y_coord <= 50:
        break
    else:
        print("Coordonatele patratului trebuie sa fie intre 10 si 50.")

# introducerea coordonatelor punctului "R"
while True:
    rx = int(input(
        f"Introduceti coordonata x a punctului R ({x_coord-x_coord+1}-{x_coord-1}): "))
    ry = int(input(
        f"Introduceti coordonata y a punctului R ({y_coord-y_coord+1}-{y_coord-1}): "))
    if x_coord >= rx <= x_coord+9 and y_coord >= ry <= y_coord+9:
        break
    else:
        print("Coordonatele punctului R trebuie sa fie in interiorul patratului.")

# afisarea patratului
for y in range(y_coord-y_coord, y_coord):
    for x in range(x_coord-x_coord, x_coord):
        if abs(x - rx) <= 1 and abs(y - ry) <= 1:
            if x == rx and y == ry:
                print("R", end=" ")
            else:
                print("+", end=" ")
        else:
            print(".", end=" ")
    print()

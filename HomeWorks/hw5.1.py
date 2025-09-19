from HomeWorks.hw5 import Distance

if __name__ == "__main__":
    d1 = Distance(10, "m")
    d2 = Distance(2, "km")
    d3 = Distance(500, "cm")
    d4 = Distance(1000, "mm")

    print(d1)
    print(d2)
    print(d3)
    print(d4)

    print("\nСложение:")
    print(d1 + d2)
    print(d2 + d3)
    print(d3 + d4)


    print("\nВычитание:")
    print(d2 - d1)
    print(d1 - d3)
    print(d3 - d4)

    print("\nСравнения:")
    print(d1 == d3)
    print(d2 > d1)
    print(d4 < d3)

    print("\nКонвертация:")
    print(f"{d2.value} {d2.unit} = {d2.convert('m')} m")
    print(f"{d3.value} {d3.unit} = {d3.convert('km')} km")

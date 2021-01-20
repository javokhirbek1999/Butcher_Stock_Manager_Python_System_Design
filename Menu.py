
st = {
    "Beef": 0,
    "Chicken": 0,
    "Lamb": 0
}
def add_to_stock():
    print("\n1.\tAdd Beef" +
          "\n2.\tAdd Chicken Meat" +
          "\n3.\tAdd Lamb Meat" +
          "\n4.\tShow Stock" +
          "\n5.\tBack")

    choice = int(input("> "))

    if choice == 1:
        weight = float(input("Enter Weight (KG): "))
        st["Beef"] += weight
        print(str(weight) + " kg of Beef has been added to the stock")
        add_to_stock()
    elif choice == 2:
        weight = float(input("Enter Weight (KG): "))
        st["Chicken"] += weight
        print(str(weight) + " kg of Chicken has been added to the stock")
        add_to_stock()
    elif choice == 3:
        weight = float(input("Enter Weight (KG): "))
        st["Lamb"] += weight
        print(str(weight) + " kg of Lamb has been added to the stock")
        add_to_stock()
    elif choice == 4:
        show_stock()
    elif choice == 5:
        main_menu()
    else:
        print("Invalid Choice")
        add_to_stock()

def sell():
    print("\n1.\tSell Beef" +
          "\n2.\tSell Chicken Meat" +
          "\n3.\tSell Lamb Meat" +
          "\n4.\tShow Stock" +
          "\n5.\tBack")

    choice = int(input("> "))

    if choice == 1:
        weight = float(input("Enter Weight (KG): "))
        st["Beef"] -= weight
        print(str(weight) + " kg of Beef has been sold")
        sell()
    elif choice == 2:
        weight = float(input("Enter Weight (KG): "))
        st["Chicken"] -= weight
        print(str(weight) + " kg of Chicken has been sold")
        sell()
    elif choice == 3:
        weight = float(input("Enter Weight (KG): "))
        st["Lamb"] -= weight
        print(str(weight) + " kg of Lamb has been sold")
        sell()
    elif choice == 4:
        show_stock()
    elif choice == 5:
        main_menu()
    else:
        print("Invalid Choice")
        sell()

def show_stock():
    ls = ["Beef", "Chicken", "Lamb"]
    j = 0
    for i in st.values():
        print(ls[j] + ": " + str(i) + " kg")
        j += 1

    print("\n1.\tMain Menu" +
          "\n2.\tExit")
    choice = int(input("> "))
    if choice == 1:
        main_menu()
    elif choice == 2:
        pass
    else:
        print("Invalid Choice")
        show_stock()

def main_menu():

    print("Main Menu: " +
              "\n1.\tAdd " +
              "\n2.\tSell " +
              "\n3.\tCheck the Stock" +
              "\n4.\tExit\n")
    choice = int(input("> "))
    if choice == 1:
       add_to_stock()
    elif choice == 2:
       sell()
    elif choice == 3:
       show_stock()
    elif choice == 4:
       pass
    else:
        print("Invalid choice")
        main_menu()

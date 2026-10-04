stock = {"boxes": 120, "tape": 45, "labels":300}

while True:
    print("\n--- Warehouse Stock Tracker---")
    print("1. View stock")
    print("2. Add item")
    print("3. Remove item")
    print("4. Quit")


    choice = input("Choose an option:  ")

    if  choice == "1":
        print(stock)


    elif choice == "2":
        item = input("Item name: ").strip().lower()
        qty = int(input("Quantity: "))
        stock[item] = stock.get(item,0) + qty
        print(f"Added {qty} to {item}.")


    elif choice == "3":
        item = input("Item name : ").strip().lower()


        if item not in stock :
            print(f"{item} not found in stock. ")
            continue


        qty = int(input("Quantity to remove : "))

        if qty >= stock[item]:
            del stock[item]
            print(f"{item} removed completely . ")
        else:
            stock[item] -= qty
            print(f"Removed {qty} from {item}. ")


    elif choice == "4":
        break   


    else:
        print("Invalid choice, try again. ")

print("Program closed")


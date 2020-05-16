import csv


class HardwareManager:
    def __init__(self, hardware, purchaseYear, user, location):
        self.hardware = hardware
        self.purchaseYear = purchaseYear
        self.user = user
        self.location = location


print("Hardware Manager")
records = []
starter = True

while starter:
    print()
    print("------------------------")
    print("(A)dd a new record")
    print("(L)ist existing records")
    print("(E)xport to CSV")
    print("(Q)uit")

    option = input("Your choice: ").upper()

    if option == "A":
        hardware = input("Hardware: ")
        purchaseYear = input("Purchase Year: ")
        user = input("User: ")
        location = input("Location: ")
        if hardware.strip() != "" and purchaseYear.strip() != "" and user.strip() != "" and location.strip() != "":
            while location.strip().upper() not in {"HOME", "OFFICE"}:
                location = input("Invalid location! Enter Home (or) Office: ")
            obj = HardwareManager(hardware, purchaseYear, user, location)
            records.append(obj)
            print(
                hardware + " (" + purchaseYear + ") has been recorded as assigned to " + user + " and retained at " + location)
        else:
            print("No record has been recorded.")
    elif option == "L":
        if len(records) == 0:
            print("No records found to display!")
        else:
            for index, i in enumerate(records):
                print(str(index + 1) + ". " + i.hardware + " (" + i.purchaseYear + ") - " + i.user + ", " + i.location)
    elif option == "E":
        if len(records) == 0:
            print("No records found to export!")
        else:
            with open('hardware.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["S. No", "Hardware", "Purchase year", "User", "Location"])
                for index, i in enumerate(records):
                    row = [index + 1, i.hardware, i.purchaseYear, i.user, i.location]
                    writer.writerow(row)
            print("Records saved as hardware.csv")
    elif option == "Q":
        print("Thank you!")
        starter = False
    else:
        print("Invalid choice! Please enter again!!")

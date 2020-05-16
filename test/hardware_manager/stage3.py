class HardwareManager:
    def __init__(self, hardware, purchaseYear, user, location):
        self.hardware = hardware
        self.purchaseYear = purchaseYear
        self.user = user
        self.location = location


print("Hardware Manager")
file1 = open("hardware.txt", "r+")
print(file1.read())

records = []
starter = True

while starter:
    hardware = input("Hardware: ")
    purchaseYear = input("Purchase Year: ")
    user = input("User: ")
    location = input("Location: ")

    if hardware.strip() != "" and purchaseYear.strip() != "" and user.strip() != "" and location.strip() != "":
        while location.strip().upper() not in {"HOME", "OFFICE"}:
            location = input("Invalid location! Enter Home (or) Office: ")
        obj = HardwareManager(hardware, purchaseYear, user, location)
        records.append(obj)
        print(hardware + " (" + purchaseYear + ") has been recorded as assigned to " + user + " and retained at " + location)
    else:
        print("No record has been recorded.")

    option = input("Do you wish to enter another record? (Y/N): ").upper()

    if option == "N":
        file1 = open("hardware.txt", "a")
        for index, i in enumerate(records):
            print(str(index + 1) + ". " + i.hardware + " (" + i.purchaseYear + ") - " + i.user + ", " + i.location)
            file1.write(str(index + 1) + ". " + i.hardware + " (" + i.purchaseYear + ") has been recorded as assigned to " + i.user + " and retained at " + i.location + "\n")
        file1.close()
        print("Records saved as hardware.txt")
        print("Thank you!")
        starter = False
    elif option == "Y":
        starter = True
    else:
        while option != "Y" or option != "N":
            print("Invalid choice! Please enter again!!")
            option = input("Do you wish to enter another record? (Y/N): ").upper()
            if option == "Y":
                starter = True
                break
            elif option == "N":
                starter = False
                for index, i in enumerate(records):
                    print(str(index + 1) + ". " + i.hardware + " (" + i.purchaseYear + ") - " + i.user + ", " + i.location)
                print("Thank you!")
                break

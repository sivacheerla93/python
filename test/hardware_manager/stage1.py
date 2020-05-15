class HardwareManager:
    def __init__(self, hardware, purchaseYear, user, location):
        self.hardware = hardware
        self.purchaseYear = purchaseYear
        self.user = user
        self.location = location


print("Hardware Manager")
records = []
starter = "Y"

while starter == "Y":
    hardware = input("Hardware: ")
    purchaseYear = input("Purchase Year: ")
    user = input("User: ")
    location = input("Location: ")
    obj = HardwareManager(hardware, purchaseYear, user, location)
    records.append(obj)
    print(hardware + " (" + purchaseYear + ") has been recorded as assigned to " + user + " and retained at " + location)

    option = input("Do you wish to enter another record? (Y/N): ").upper()

    if option == "N":
        for index, i in enumerate(records):
            print(str(index + 1) + ". " + i.hardware + " (" + i.purchaseYear + ") - " + i.user + ", " + i.location)
        print("Thank you!")
        starter = "N"
    elif option == "Y":
        starter = "Y"
    else:
        starter2 = True
        while starter2:
            print("Invalid choice! Please enter again!!")
            option2 = input("Do you wish to enter another record? (Y/N): ").upper()

            if option2 == "Y":
                starter2 = False
                starter = "Y"
            elif option2 == "N":
                starter2 = False
                starter = "N"
                for index, i in enumerate(records):
                    print(str(index + 1) + ". " + i.hardware + " (" + i.purchaseYear + ") - " + i.user + ", " + i.location)
                print("Thank you!")
            else:
                starter2 = True

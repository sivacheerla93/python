import csv
import datetime


class HardwareManager:
    def __init__(self, hid, hardware, purchaseYear, user, location, createdDate, updatedDate):
        self.hid = hid
        self.hardware = hardware
        self.purchaseYear = purchaseYear
        self.user = user
        self.location = location
        self.createdDate = createdDate
        self.updatedDate = updatedDate


print("Hardware Manager")
records = []
starter = True
hid = 0

while starter:
    print()
    print("------------------------")
    print("(A)dd a new record")
    print("(L)ist existing records")
    print("(C)hange user/location")
    print("(D)elete a record")
    print("(E)xport to CSV")
    print("(Q)uit")

    option = input("Your choice: ").upper()

    if option == "A":
        hid = hid + 1
        hardware = input("Hardware: ")
        purchaseYear = input("Purchase Year: ")
        user = input("User: ")
        location = input("Location: ")
        createdDate = datetime.datetime.now()
        updatedDate = datetime.datetime.now()
        if hardware.strip() != "" and purchaseYear.strip() != "" and user.strip() != "" and location.strip() != "":
            while location.strip().upper() not in {"HOME", "OFFICE"}:
                location = input("Invalid location! Enter Home (or) Office: ")
            obj = HardwareManager(hid, hardware, purchaseYear, user, location, createdDate, updatedDate)
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
                print(str(i.hid) + ". " + i.hardware + " (" + i.purchaseYear + ") - " + i.user + ", " + i.location)
                print("   Created: " + i.createdDate.strftime("%A") + ", " + i.createdDate.strftime("%d") + ". " + i.createdDate.strftime("%B") + " " + i.createdDate.strftime("%Y") +" " +  i.createdDate.strftime("%I") + ":" + i.createdDate.strftime("%M") + i.createdDate.strftime("%p"))
                print("   Updated: " + i.updatedDate.strftime("%A") + ", " + i.updatedDate.strftime(
                    "%d") + ". " + i.updatedDate.strftime("%B") + " " + i.updatedDate.strftime(
                    "%Y") + " " + i.updatedDate.strftime("%I") + ":" + i.updatedDate.strftime(
                    "%M") + i.updatedDate.strftime("%p") + "\n")
    elif option == "C":
        did = int(input("Enter record ID: "))
        for i in records:
            if i.hid == did:
                name = input("Enter a new user: ")
                loc = input("Enter a new location (Home/Office): ")
                if loc.upper() not in {"HOME", "OFFICE"}:
                    print("Invalid location! Please try again!!")
                    starter = True
                i.user = name
                i.location = loc
                i.updatedDate = datetime.datetime.now()
                print(i.hardware + " (" + i.purchaseYear + ") has been updated.")
            else:
                print("There are no records with the ID " + "'" + str(did) + "'.")
                starter = True
    elif option == "D":
        did = int(input("Enter record ID: "))
        for i in records:
            if i.hid == did:
                print("You are about to delete " + i.hardware + " (" + i.purchaseYear + ") - " + i.user + ", " + i.location)
                opt = input("Do you wish to delete this record (Y/N): ").upper()
                if opt == "Y":
                    records.remove(i)
                    print("Record deleted.")
                elif opt == "N":
                    starter = True
                else:
                    print("Invalid option! Please try again!!")
                    starter = True
    elif option == "E":
        if len(records) == 0:
            print("No records found to export!")
        else:
            with open('hardware2.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["S. No", "Hardware", "Purchase year", "User", "Location", "Created Date", "Updated Date"])
                for index, i in enumerate(records):
                    cd = i.createdDate.strftime("%A") + ", " + i.createdDate.strftime("%d") + ". " + i.createdDate.strftime("%B") + " " + i.createdDate.strftime("%Y") +" " +  i.createdDate.strftime("%I") + ":" + i.createdDate.strftime("%M") + i.createdDate.strftime("%p")
                    ud = i.updatedDate.strftime("%A") + ", " + i.updatedDate.strftime("%d") + ". " + i.updatedDate.strftime("%B") + " " + i.updatedDate.strftime("%Y") +" " +  i.updatedDate.strftime("%I") + ":" + i.updatedDate.strftime("%M") + i.updatedDate.strftime("%p")
                    row = [i.hid, i.hardware, i.purchaseYear, i.user, i.location, cd, ud]
                    writer.writerow(row)
            print("Records saved as hardware.csv")
    elif option == "Q":
        print("Thank you!")
        starter = False
    else:
        print("Invalid choice! Please enter again!!")

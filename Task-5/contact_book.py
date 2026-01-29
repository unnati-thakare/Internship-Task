contacts = []

while True:
    print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
    ch = input("Choose: ")

    if ch == "1":
        contacts.append({
            "name": input("Name: "),
            "phone": input("Phone: "),
            "email": input("Email: "),
            "address": input("Address: ")
        })
        print("Added")

    elif ch == "2":
        for c in contacts:
            print(c["name"], "-", c["phone"])

    elif ch == "3":
        key = input("Search name/phone: ")
        for c in contacts:
            if key in c["name"] or key in c["phone"]:
                print(c)

    elif ch == "4":
        name = input("Name to update: ")
        for c in contacts:
            if c["name"] == name:
                c["phone"] = input("Phone: ")
                c["email"] = input("Email: ")
                c["address"] = input("Address: ")
                print("Updated")

    elif ch == "5":
        name = input("Name to delete: ")
        contacts = [c for c in contacts if c["name"] != name]
        print("Deleted")

    elif ch == "6":
        break

    else:
        print("Invalid")

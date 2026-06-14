name = input("What is your name? ")
match name:
    case "harry" | "hermione" | "ron":
        print("griffindor")
    case "draco":
        print("slytherin")
    case "luna":
        print("ravenclaw")
    case _:
        print("not found")
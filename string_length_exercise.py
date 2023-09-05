name = input("Name of Person:  ")
if len(name) < 3:
    print("Error! Name must be at least 3 characters long")
elif len(name) > 50:
    print("Error! Name must not be more than 50 characters long")
else:
    print("Looks Good! " + name)

name =input("Name of Person: ")
while 3 < len(name) and len(name) < 50:
        print("looks good!  " + name)
        print(" Keep practicing!!!")

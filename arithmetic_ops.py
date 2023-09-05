print(10 * 3) #multiplication
print(10 // 3) #division with int as result

x = (10 / 3) #division with floar as result
print(abs(-x))

print(10 % 3) #modulus gives a remainder
print(10 ** 3) #exponent (to the power of)
print(10 + 3) # simple addition

x = 10
d= x + 3
print(d)
d = d * x
print(d)

x = 17
x -=7
print(x)


# weight conversion program gpt corrected!!


choice = input("Choose between l and k: ")

if choice == "l":
    weight_in_lbs = float(input("Lbs: "))
    weight_in_kgs = weight_in_lbs * 0.45
    print("YOUR WEIGHT IN KILOS IS " + str(weight_in_kgs))
elif choice == "k":
    weight_in_kgs = float(input("Kgs: "))
    weight_in_lbs = weight_in_kgs * 2.20
    print("YOUR WEIGHT IN POUNDS IS " + str(weight_in_lbs))
else:
    print("Invalid choice. Please choose either 'l' or 'k'.")
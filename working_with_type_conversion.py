

#weight conversion program

chiiswa = input("Choose between l and k: ")

if chiiswa == "l":
    weight_in_lbs = input("weight in pounds:   ")
    weight_in_kgs= int(weight_in_lbs) * 0.45
    print("YOUR WEIGHT IN KILOS IS  " + str(weight_in_kgs))
elif chiiswa == "k":
    weight_in_kgs= input("weight in kgs:  ")
    weight_in_lbs= int(weight_in_kgs) * 2.20
    print("YOUR WEIGHT IN POUNDS IS  " + str(weight_in_lbs))
else:
    print("Invalid choice! Choose between l and k ")

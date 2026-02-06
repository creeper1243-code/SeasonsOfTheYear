month = int(input("What month is it? tell me here ---> "))

if 2 < month < 6:
    print("its spring!")

elif 5 < month < 9:
    print("its summer!")

elif 8 < month < 12:
    print("its fall!")

elif 0 < month < 3 or month == 12:
    print("its winter!")
else:
    print("this month dont exist yet gng")
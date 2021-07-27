#Check if magician and expert is true case yes print: "Master Magician"
is_magician = False
is_expert = True

if is_magician or is_expert:
    # Check is magician or expert
    if is_magician and is_expert:
        #Check is magician and expert
        print(100 * '+')
        print('Master Magician!')
        print(100 * '+')
    elif is_magician and not is_expert:
        # Check is magician
        print("At least you're getting there")
    elif is_expert and not is_magician:
        # Check is expert
        print("You need magician powers")
else:
    # If not is magician and not is expert
    print("You don't has permission")

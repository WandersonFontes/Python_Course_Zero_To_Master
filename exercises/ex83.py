#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.

def checkDriverAge(age=None):
    if age == None:
        print("Please, inset your age!")
    elif str(type(age)) != str(type(1)):
        print('Sorry.\nValue Invalid!')
    elif int(age) < 18:
        print(f"Your age is {age}.\nSorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print(f"Your age is {age}.\nPowering On. Enjoy the ride!");
    elif int(age) == 18:
        print(f"Your age is {age}.\nCongratulations on your first year of driving. Enjoy the ride!")


checkDriverAge(18)
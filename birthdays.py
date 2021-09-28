def birthdays(d):
    if d == "swathi":
        return ("swathi birthday is 19/11/2000")
    elif d == "swapna":
        return ("swapna birthday is 28/06/1997")
    elif d == "swetha":
        return ("Swetha birthday is 23/10/1999")
    else:
        return ("%s is not in the list" % d)


print("Welcome to the birthday dictionary. We know the birthdays of:")
d = input("Swathi \nswapna \nswetha\n")
print(birthdays(d))

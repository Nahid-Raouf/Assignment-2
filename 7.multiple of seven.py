number = int(input("Enter the number: "))
if (number % 7 == 0):
    print(number ,": it is a multiple of seven.")
else:
    result = 7 - number % 7 + number 
    print (number ,': it is not a multiple of seven.\n',result,': the next  multiple of seven.')
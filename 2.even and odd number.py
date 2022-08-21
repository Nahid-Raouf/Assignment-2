number = int(input("Enter the number"))
odd = 0
even = 0
while number != 0:
    num = number % 10

    if num % 2 == 0:
        even += 1

    else:
        odd += 1
    number //= 10 

print("The number even: ",even)
print ("The number odd: ",odd )
if even == odd :
    print ("your even and odd number are equal.")
elif even > odd :
    print ("your number of even digits is more.")
else:
    print ("your number of odd digits is more.")


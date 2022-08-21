number = (int(input("Enter your number: ")))
num = number
reverse = 0
while (number > 0):
    num2 = number % 10
    reverse = ((reverse * 10) + num2)
    number //= 10
if num == reverse:
    print(reverse , ' : number and reverse are equal.')
else:
    print(reverse , ' : the number and the reverse are not equal.')
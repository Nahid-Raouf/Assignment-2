username = "Nahid"
password = "Nahid_R.s"
user = input("Username:")
pas = input("Password:")
if user == username and pas == password:
    print("Wellcome")
else:
    print ("The username and password are wrong.")
    c=0
    while c<=3:
        user = input("Username:")
        pas = input("Password:")
        print ("The username and password are wrong. Please try again")
        c=c+1
        if c == 3 :
           print("Warning! Account locked")

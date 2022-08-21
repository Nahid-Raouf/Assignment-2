temperature = float(input("enter the temperature : "))

Tempreture1 = int(input('choose your scail1 :\n 1.celsius \n 2.kelvin \n 3.fahrenheit \n '))
Tempreture2 = int(input('choose your scail2 :\n 1.celsius \n 2.kelvin \n 3.fahrenheit \n '))

if Tempreture1 == 1 and Tempreture2 == 2:
    print('com = ',(temperature + 273.15),'K')

elif Tempreture1 == 2 and Tempreture2 == 1:
    print ('com = ',(temperature - 273.15),'C')

elif Tempreture1 == 1 and Tempreture2 == 3:
    print ("com = ",(temperature * 1.8) + 32 , 'F')

elif Tempreture1 == 3 and Tempreture2 == 1:
    print ('com = ',(temperature - 32) / 1.8 ,'C')

elif Tempreture1 == 3 and Tempreture2 == 2:
    print ('com = ',((temperature + 459.67) / 1.8),'K')
'''List of all Tasks can be viewed on School website:
https://win.ae.gems-fusion.com/files/sc3420/sc3420388/114/[41854]0478_S20_PRE_Release.pdf
'''

#Declaration of fixed variables
price = 0
days_in_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

#Asking user input for variables, with error checking provided
day = input('What day is it? ')
day_lower = day.lower()
while day_lower not in days_in_week:
    print('Please enter a valid date: ')
    day = input('What day is it? ')
    day_lower = day.lower()
    
hour = int(input('What hour of the day is it? '))
while hour < 8 or hour >= 24:
    print('Cannot park during the hours 1-8: ')
    hour = int(input('What hour of the day is it?'))
    
parking_time = int(input('How long are you keeping your car parked (in hours): '))

#Error Verification (to make sure parking time doesn't exceed maximum hours of stay)
while day_lower == ('sunday') and parking_time > 8:
    print('Parking time cannot exceed 8 hours on a Sunday')
    parking_time = int(input('How long are you keeping your car parked'))

while day_lower == ('saturday') and parking_time > 4:
    print('Parking time cannot exceed 4 hours on a Saturday')
    parking_time = int(input('How long are you keeping your car parked'))
        
while day_lower != ('saturday') and day_lower != ('sunday') and parking_time > 2:
    print('Parking time cannot exceed 2 hours on days, Monday - Friday')
    parking_time = int(input('How long are you keeping your car parked'))

while hour + parking_time > 24:
    print('Cannot park beyond midnight')
    parking_time = int(input('How long are you keeping your car parked'))

#Calculating and making prices fair
if hour >= 16:
    price = 2
    diff= 0
    
else:
    diff = 16 - hour

    
if hour + parking_time > 16:
        if day_lower == 'sunday':
            price = (diff * 2) + 2

        elif day_lower == 'saturday':
            price = (diff * 3) + 2

        else:
            price = (diff * 10) + 2

else:
    if day_lower == 'sunday':
        price = parking_time * 2
        
    elif day_lower == 'saturday':
        price = parking_time * 3
        
    else:
        price = parking_time * 10

#Valid Frequent Parking Number for testing purposes: 12343
frequent_parking_number = str(input("Please type your frequent parking number (5 digits) If you do not have one, please type '0': "))
    
        
#Verifying the Modulo 11/Check Digit
if len(frequent_parking_number) != 5:
    print("No discount code added")
    discount = False
else:
    d1 =int(frequent_parking_number[0])*5
    d2 =int(frequent_parking_number[1])*4
    d3 =int(frequent_parking_number[2])*3
    d4 =int(frequent_parking_number[3])*2
    d5 =int(frequent_parking_number[4])

    Sum =(d1 + d2 + d3 + d4)
    Mod = 11 - (Sum % 11)

    if d5 == Mod:
        print("Discount added")
        discount = True
    elif d5 != Mod:
        print("Not a true code")
        discount = False


#Adding the discount
if hour >= 16 and discount == True:
    price = price / 2
elif hour >= 8 and discount == True:
    price = price * 0.9

#Printing the final price (Additional: adding a dollar sign before price)
price = '${}'.format(price)
print('The amount to be paid is:', price)

'''Note:
More error prevention methods could have been added such as the rounding down of
the hours of day. Though, this would require importing a library and isn't part of the
task requirements, so have been ommited'''

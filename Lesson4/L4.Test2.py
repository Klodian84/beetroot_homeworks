
# The Valid Phone number program.

phone_number = input('Please enter your 10 digit phone number: ')

if len(phone_number) % 10 == 0 and phone_number.isdigit():
    print( phone_number)
elif len(phone_number) % 10 != 0:
    print('Please make sure you are writing a correct 10 digit number')


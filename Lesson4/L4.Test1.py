#String Manipulation

s = input ("Enter a string,Options, helloworld, my, x: ")

if len(s) >= 2:
    print(s[:2] + s[-2:])
elif len(s) < 2:
    print('Empty String')




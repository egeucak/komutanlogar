import random
garavel = open("adim garavel.txt", "r", encoding='cp1254').read().splitlines()
for i in range(10):
	x = 0
	while (x == 0):
		secilen = random.choice(garavel).strip()
		if (len(secilen) > 0):
			x = 1
	if "=" in secilen:
		secilen = secilen.split("=")[1]
	print(secilen)

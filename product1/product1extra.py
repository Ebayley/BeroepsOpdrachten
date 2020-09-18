x = 3
y = 2

while x > y:	
	print("Hello You!, ik ben Elona")
	name = input("Wie ben jij? ")
	print("Hello " + name)
	import datetime
	t = datetime.datetime.now()
	print("De datum en tijd is: " + t.strftime("%c"))
	
    
    
	while x > y:
	    a = input('Wil je dit programma nog een keer doen? type Y/N\n')  	
	    if a == 'N':
		    print('Doei!!!\n')
		    x = 1
	    elif a == 'Y':
		    print('\n')
		    break
	    else:
		    print('Type Y or N')
		    break	
while True:
    import random
    
    guess = int(input("Raad een nummer tussen de 1 en de 10:\n"))
    randomNumber = random.randint(1,10)
    print("Jij raadde: " + str(guess))
    print("Het was: " + str(randomNumber))

    if randomNumber == guess:
        print("\nJe hebt goed geraden")
        break
    else:
        print("\nJe raadde dus verkeerd.\n")

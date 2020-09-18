x = 3
y = 2

while True:
	print("\nHello You!, ik ben Elona")
	name = input("\nWie ben jij? \n")
	print("\nHallo " + name)
	import datetime
	t = datetime.datetime.now()
	print("\nDe datum en tijd is: " + t.strftime("%c"))


	print("\nHier zijn een aantal vragen over mij om me beter te leren kennen.")

	def eersteVraag():
		v1 = input("\nKies A, B of C:\n")
		if v1 == 'A':
		    	print('\nCorrect, mijn hond heet Bruce')
		    	x = 1
		elif v1 == 'B':
		    	 print('\nNee! ik heb een hond, hij heet Bruce')
		elif v1 == 'C':
			 print('\nNee! ik heb een huisdier, een hond en hij heet Bruce.')
		else:
			print('\n(Let op! het moeten hoofdletters zijn.)')
			eersteVraag()

	def tweedeVraag():
		v2 = input("\nKies A, B of C:\n")
		if v2 == 'A':
		    	print('\nCorrect, dat zijn inderdaad mijn hobbies!')
		    	x = 1
		elif v2 == 'B':
		    	 print('\nNee! fout, A was het juiste antwoord')
		elif v2 == 'C':
			 print('\nlol, A was het goede antwoord')
		else:
			print('\n(Let op! het moeten hoofdletters zijn.)')
			tweedeVraag()	

	def derdeVraag():
		v3 = input("\nKies A, B of C:\n")
		if v3 == 'A':
		    	print('\nFout! ik heb een zus én een broer.')
		    	x = 1
		elif v3 == 'B':
		    	 print('\nJe hebt het juist, ik heb een oudere broer en een tweeling zus.')
		elif v3 == 'C':
			 print('\nNee, ik heb een zus en een broer.')
		else:
			print('\n(Let op! het moeten hoofdletters zijn.)')
			derdeVraag()	




	print("\n\n1. Heb ik een huisdier?\n")
	print("A. Ja, je hebt een hond.\nB. Ja, je hebt een kat.\nC. Nee, je hebt geen huisdier.")	
	eersteVraag()
	print("\n\n2. Wat zijn mijn hobbies?")
	print("\nA. Ik denk dat je hobbies gamen, tekenen en lezen zijn.\nB. Ik denk dat je hobbies tekenen, gamen en schrijven zijn.\nC. Ik denk dat je geen hobbies hebt.")
	tweedeVraag()
	print("\n\n3. Heb je broers of zussen?")
	print("A. Ja, je hebt een zus of een broer.\nB. Ja, je hebt een zus en een broer.\nC. Nee, je hebt geen broers of zussen.")
	derdeVraag()

	a = input('Wil je dit programma nog een keer doen? type Y/N\n')
	if a == 'N':
		print('Doei!')
		break		
	elif a == 'Y':
		print('okay')
	else:
		print('Typ Y of N') 
	


x = True

while x == True:
	import os
	os.system('cls')

	print("______________________________________________________________________________________________________")
	print("\n Hello You! ik ben Elona.")
	name = input(" Wie ben jij? \n\n")
	print("______________________________________________________________________________________________________")
	print("\n Hallo " + name)
	import datetime
	t = datetime.datetime.now()
	print("\n De datum en tijd is: " + t.strftime("%c"))
	print("______________________________________________________________________________________________________")


	print("\n Hier zijn een aantal vragen over mij om me beter te leren kennen.")
	
	def vijfdeVraag():
		v5 = input("\n Kies A, B of C:\n")
		if v5 == 'A':
			print("\n Fout! hij is 7 of 6, we weten het niet precies omdat hij uit een asiel in Spanje komt.\n Daar was hij een tijdje een staathond.")
		elif v5 == 'B':
			print("\n We weten niet precies hoe oud hij is omdat hij uit een asiel in Spanje komt.\n Daar was hij een tijdje een staathond.")
		elif v5 == 'C':
			print("\n We weten niet precies hoe oud hij is omdat hij uit een asiel in Spanje komt.\n Daar was hij een tijdje een staathond.")
		else:
			print('\n(Let op! het moeten hoofdletters zijn.)')
			vijfdeVraag()

	def vierdeVraag():
		v4 = input("\n Kies A, B of C:\n")
		if v4 == 'A':
			print("\n Fout!, zijn Naam is nu Bruce, maar zijn naam was Brubakker toen hij naar Nederland kwam. hij is toen in het asiel Bruce genoemd.")
		elif v4 == 'B':
			print("\n Nee, zijn naam was in het ooit Brubakker. Toen hij naar Nederland kwam is hij in het asiel Bruce genoemd.")
		elif v4 == 'C':
			print("\n Correct! zijn naam was vroeger Brubakker. Toen hij naar Nederland kwam is hij in het asiel Bruce genoemd.")
		else:
			print('\n(Let op! het moeten hoofdletters zijn.)')
			vierdeVraag()

			
			
	def eersteVraag():
		v1 = input("\n Kies A, B of C:\n")
		if v1 == 'A':
		    	print('\n Correct, mijn hond heet Bruce')
		elif v1 == 'B':
		    	 print('\n Nee! ik heb een hond, hij heet Bruce')
		elif v1 == 'C':
			 print('\n Nee! ik heb een huisdier, een hond en hij heet Bruce.')
		else:
			print('\n(Let op! het moeten hoofdletters zijn.)')
			eersteVraag()




	def tweedeVraag():
		v2 = input("\n Kies A, B of C:\n")
		if v2 == 'A':
		    	print('\n Correct, dat zijn inderdaad mijn hobbies!')
		elif v2 == 'B':
		    	 print('\n Nee! fout, A was het juiste antwoord')
		elif v2 == 'C':
			 print('\n lol, A was het goede antwoord')
		else:
			print('\n(Let op! het moeten hoofdletters zijn.)')
			tweedeVraag()	




	def derdeVraag():
		v3 = input("\n Kies A, B of C:\n")
		if v3 == 'A':
		    	print('\n Fout! ik heb een zus én een broer.')
		elif v3 == 'B':
		    	 print('\n Je hebt het juist, ik heb een oudere broer en een tweeling zus.')
		elif v3 == 'C':
			 print('\n Nee, ik heb een zus en een broer.')
		else:
			print('\n(Let op! het moeten hoofdletters zijn.)')
			derdeVraag()	

	def hondOfMens():
		hm = input("\n Kies A, B of C:\n")
		if hm == 'A':
			print("\n Dat snap ik best wel.")
		elif hm == 'B':
			print("______________________________________________________________________________________________________")
			print("\n Goede keuze, mijn hond is heel schattig.\n\n Hier zijn een aantal vragen over mijn hond.\n Zodat je hem beter kan leren kennen.")
			print("______________________________________________________________________________________________________")
			print("\n Was Bruce zijn naam altijd Bruce?")
			print("\n A. Nee, zijn naam is Brucie. Niet Bruce.\n B. Ja, zijn naam is altijd Bruce geweest.\n C. Nee, zijn naam was iets anders.")
			vierdeVraag()
			print("______________________________________________________________________________________________________")
			print("\n Hoe oud is Bruce?")
			print("\n A. Ik denk dat hij 5 is.\n B. Ik denk dat hij 6 is.\n C. Ik denk dat hij 7 is.")
			vijfdeVraag()
			print("______________________________________________________________________________________________________")
			print("\n Nu weet je meer over mijn hond! Ik hoop dat je het leuke vragen vondt.\n")
		
		elif hm == 'C':
			print("______________________________________________________________________________________________________")
			print("\n Okay, Ik had zelf voor mijn super schattige, super leuke hond Brucie gekozen.\n Hier zijn een aantal vragen om mij beter te leren kennen.")
			print("\n\n Wat zijn mijn hobbies?")
			print("\n A. Ik denk dat je hobbies gamen, tekenen en lezen zijn.\n B. Ik denk dat je hobbies tekenen, gamen en schrijven zijn.\n C. Ik denk dat je geen hobbies hebt.")
			tweedeVraag()
			print("______________________________________________________________________________________________________")
			print("\n\n Heb ik broers of zussen?")
			print("\n A. Je hebt een zus of een broer.\n B. Je hebt een zus en een broer.\n C. Je hebt geen broers of zussen.")
			derdeVraag()
			print("______________________________________________________________________________________________________")
			print("\n Nu weet je meer over mij. Ik hoop dat je het leuke vragen vondt.\n")				
			
		else:
			print('\n(Let op! het moeten hoofdletters zijn.)')
			hondOfMens()



	print("______________________________________________________________________________________________________")
	print("\n\n Heb ik een huisdier?\n")
	print(" A. Ja, je hebt een hond.\n B. Ja, je hebt een kat.\n C. Nee, je hebt geen huisdier.")	
	eersteVraag()
	print("______________________________________________________________________________________________________")
	print("\n Wil je meer over mijn hond weten? of meer over mij?\n")
	print("\n A. Ik wil nergens meer over weten.\n B. Ja, ik wil graag meer over je hond weten.\n C. Ik wil graag meer over jou weten.")
	hondOfMens()

	

	def end():
		print("______________________________________________________________________________________________________")
		a = input('\n Wil je dit programma nog een keer doen? type Y/N\n')
		if a == 'N':
			print("______________________________________________________________________________________________________")
			print('\n Okay, fijne dag!')
			print("______________________________________________________________________________________________________")
			import sys
			sys.exit()
		elif a == 'Y':
			print('\n Ok.')
		else:
			print(" typ 'Y' of 'N'")
			end()

	
	end()
	


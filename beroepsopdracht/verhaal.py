x = True

line = ("______________________________________________________________________________________________________")

while x == True:
    import os
    os.system('cls')

    #Het is me helaas niet gelukt om op tijd alles af te hebben. ik ga er nog verder aan werken. ook aan de flowchart en de microbit opdrachten


    
    def derdeVraag():
        print("\n A. Jss.\n B. ss")
        v3 = input("\n Kies A of B:\n")
        if v3 == 'A':
            print('\n a')
        elif v3 == 'B':
            print('\n b')
        else:
            print('\n(Let op! het moeten hoofdletters zijn.)')
            derdeVraag()
     

    def vierdeVraag():
        print("\n A. Ja, Ik ga alsnog opzoek naar een smokkelaar.\n B. Nee, we wachten tot het weer beter is.")
        v4 = input("\n Kies A of B:\n")
        if v4 == 'A':
            print(line)
            print('\nBAD ENDING: YOU DROWN\n\nJullie zoeken en vinden één smokkelaar.\n\nJullie vertrekken die avond. Het weer is slecht en je groep zit samen met andere groepen op de boot.\nDe boot zit veel te vol.\n\nDe boot zinkt en je verdrinkt.')
        elif v4 == 'B':
            print(line)
            print('\nWe hebben gewacht tot het weer niet meer onstuimig was. We hebben ondertussen gezocht naar smokkelaars.\nWe vonden er drie maar we hebben gekozen voor een charismatische man met tatoeages. Een Turk.\nIeder betaalt 1.500 dollar voor de boottocht en voor de bustocht naar de Turkse kustplaats - ik heb de naam niet onthouden - in de provincie Izmir.\nIn totaal heb ik 3.500 dollar op zak, dus de oversteek naar Griekenland is een flinke hap uit mijn budget. ')
            derdeVraag()
        else:
            print('\n(Let op! het moeten hoofdletters zijn.)')
            vierdeVraag()


    def tweedeVraag():
        print("\n A. Ja, ik wil met deze groep mee.\n B. Nee, deze groep is te groot. Ik wil met een andere groep mee.\n ")
        v2 = input("\n Kies A of B:\n")
        if v2 == 'A':
            print(line)
            print("\nOnze groep bestaat uit hoogopgeleide jongeren. De meesten werken als media-activist, voor een ngo, mensenrechtenorganisatie of als fotograaf.\nWe hebben onze reis nauwkeurig voorbereid. Omdat we met zoveel zijn, hebben we een groot netwerk. Kennissen, vrijwilligers en ngo's zijn op de hoogte gebracht van onze komst.\nOp deze manier hebben we onder meer het nummer bemachtigd van de Griekse kustwacht, mochten we in de problemen raken bij onze bootoversteek.\n\nIk besef dat een goede voorbereiding geen garantie biedt voor een geslaagde reis. Er kan van alles gebeuren.\nOnze boot kan zinken, we kunnen opgepakt worden door de politie. Toch probeer ik me niet al te veel zorgen te maken. Ik bekijk het van dag tot dag.\n\nWe hebben drie dagen in Istanbul gewacht. Het weer was te onstuimig om de bootoversteek naar Griekenland te maken.\nIn Istanbul hebben we een smokkelaar gevonden Dat was haast makkelijker dan het vinden van sigaretten!\nHet werkt zo: je gaat op een plek zitten waar veel koffiebarretjes zijn en binnen tien minuten zie je minstens vijf smokkelaars.\nZij zien jou ook We hebben ons opgesplitst en gesprekken gevoerd met zeven smokkelaars.\nOnze keuze is gevallen op een charismatische man met tatoeages. Een Turk.\nWe hebben twee uur koffie met hem gedronken en een deal gesloten: ieder betaalt 1.200 dollar voor de boottocht en voor de bustocht naar de Turkse kustplaats.\nIk heb de naam niet onthouden - in de provincie Izmir.\nIn totaal heb ik 3.500 dollar op zak, dus de oversteek naar Griekenland is een flinke hap uit m'n budget.\n")
            derdeVraag()
        elif v2 == 'B':
            print(line)
            print('\nJe gaat met een andere groep mee.\nHij is kleiner maar jullie zijn niet goed voorbereid.\nHet weer is onstuimig. proberen jullie alsnog een smokkelaar te vinden om over te steken?\n\n')
            vierdeVraag()
        else:
            print('\n(Let op! het moeten hoofdletters zijn.)')
            tweedeVraag()	

    def eersteVraag():
        v1 = input("\n Kies A of B:\n")
        if v1 == 'A':
            print(line)
            print('\nVanochtend met het vliegtuig aangekomen in Istanbul. Daar heb ik onze groep, bestaande uit 25 jongeren die allemaal naar Europa willen, ontmoet.\nVijf van hen komen rechtstreeks uit Latakia, de Syrische kuststrook waar de Russen en troepen van Assad nu een offensief houden.\nEen aantal komt uit Libanon, de rest uit Gaziantep. Het zijn vrienden van vrienden.\nSommigen ken ik nog uit Aleppo, waar ik woonde in de begintijd van de revolutie. De sfeer is goed, we praten over vroeger en maken grappen.\n\nWil je met deze groep mee?\n')
            tweedeVraag()
        elif v1 == 'B':
            print(line)
            print('\nJe hebt ervoor gekozen om in Gaziantep te blijven, maar er is daar voor jou geen toekomst. Je kunt geen werk vinden.\n\nJe besluit om alsnog te vertrekken. \nVanochtend met het vliegtuig aangekomen in Istanbul. Daar heb ik onze groep, bestaande uit 25 jongeren die allemaal naar Europa willen, ontmoet.\nVijf van hen komen rechtstreeks uit Latakia, de Syrische kuststrook waar de Russen en troepen van Assad nu een offensief houden.\nEen aantal komt uit Libanon, de rest uit Gaziantep. Het zijn vrienden van vrienden.\nSommigen ken ik nog uit Aleppo, waar ik woonde in de begintijd van de revolutie. De sfeer is goed, we praten over vroeger en maken grappen.\n\nWil je met deze groep mee?\n')
            tweedeVraag()
        else:
            print('\n(Let op! het moeten hoofdletters zijn.)')
            eersteVraag()

    print(line)
    print("\nIn deze applicatie ga je het verhaal van De Syrische fotograaf Mohammad Abdulazez volgen. Hij is vanuit de Turkse grensplaats Gaziantep naar Nederland gevlucht Hij heeft tijdens zijn reis een dagboek gehouden en foto’s genomen.\n\nJe speelt alsof je Mohammad bent.")
    print(line)

    print(line)
    print("\n\n28 september\n\nGaziantep, Turkije\n\n'Net mijn ouders verteld dat ik eraan denk om te vertrekken. Ze waren verdrietig, maar zagen het aankomen.\nDe eerste rectie van mijn moeder was: je hoeft niet te gaan, blijf bij ons.\nDaarnaa zei ze ik begrijp het, ga maar. Mijn vader reageerde gelaten. Het is beter voor jou, zei hij.\n\nToen ik hier twee jaar geleden aankwam was er nog genoeg te doen. Ik werkte als fixer voor internationale media en reisde soms als fotograaf terug naar Syrië.\nMaar de media hebben hun belangstelling in het conflict verloren ngo's hebben hun duren gesloten Mijn oudste zus is, die voor een ngo werkte, is haar baan kwijt.\n\nIk verveel me hier, al mijn vrienden naar Europa vertrokken. Wachten heeft geen zin. De oorlog in Syrië zal nog jaren duren.\nVoorlopig kan ik niet terug ik wil verder met m'n even.\nHier is geen toekomst voor mij. Turkije behandelt ons als tweederangsburger Europa zal ik de duizenden vluchtelingen zijn.\nIk bereid me voor op barre omstandigheden. BEN ik gaan. Op de lange termijn zal ik het daar beter hebben\n\nVertrek jij uit Gaziantep?\n")
    print(" A. Ja, ik vertrek.\n B. Nee, ik blijf in Gaziantep.\n")	
    eersteVraag()
    print(line)


















    def end():
        print(line)
        a = input('\n Wil je dit programma nog een keer doen? type Y/N\n')
        if a == 'N':
            print(line)
            print('\n Okay, fijne dag!')
            print(line)
            import sys
            sys.exit()
        elif a == 'Y':
            print('\n Ok.')
        else:
            print(" typ 'Y' of 'N'")
            end()
    end()
	